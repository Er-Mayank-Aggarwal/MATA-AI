from fastapi import HTTPException
from pydantic import BaseModel, Field, field_validator
from typing import Optional
import uuid

from app.constants.curriculum import VALID_CLASSES, VALID_SUBJECTS, CURRICULUM, QUESTION_TYPES
from app.services.prompt_builder import build_question_prompt
from app.services.gemini_service import generate_questions
from app.services.pdf_service import create_questions_pdf, create_solutions_pdf


# ── Request Schema ─────────────────────────────────────────────────────────────

class GenerateQuestionsRequest(BaseModel):
    class_number: int = Field(..., alias="class", ge=9, le=10, description="Class 9 or 10")
    subject: str = Field(..., description="mathematics | science | social_science")
    chapter_number: int = Field(..., alias="chapter", ge=1, description="Chapter number")
    total_questions: int = Field(..., ge=1, le=50, description="Total number of questions (max 50)")
    question_distribution: Optional[dict[str, int]] = Field(
        default=None,
        description="Dict of question_type → count. E.g. {mcq: 10, short_answer: 5}"
    )
    difficulty: Optional[str] = Field(
        default="mixed",
        description="easy | medium | hard | mixed | board_exam"
    )
    extra_instructions: Optional[str] = Field(
        default="",
        max_length=1000,
        description="Additional prompt instructions from the user"
    )

    class Config:
        populate_by_name = True

    @field_validator("subject")
    @classmethod
    def validate_subject(cls, v):
        normalized = v.lower().replace(" ", "_")
        if normalized not in VALID_SUBJECTS:
            raise ValueError(f"Subject must be one of: {', '.join(VALID_SUBJECTS)}")
        return normalized

    @field_validator("question_distribution")
    @classmethod
    def validate_distribution(cls, v):
        if v is None:
            return v
        invalid_types = [k for k in v.keys() if k not in QUESTION_TYPES]
        if invalid_types:
            raise ValueError(f"Invalid question types: {invalid_types}. Valid: {list(QUESTION_TYPES.keys())}")
        if any(count < 0 for count in v.values()):
            raise ValueError("Question counts must be non-negative")
        return v


# ── Response Schema ────────────────────────────────────────────────────────────

class GenerateQuestionsResponse(BaseModel):
    request_id: str
    status: str
    data: dict


# ── Controller ─────────────────────────────────────────────────────────────────

async def handle_generate_questions(request: GenerateQuestionsRequest) -> GenerateQuestionsResponse:
    # Validate chapter exists
    subject_data = CURRICULUM.get(request.class_number, {}).get(request.subject, {})
    if not subject_data:
        raise HTTPException(status_code=400, detail=f"Invalid class/subject combination")

    chapters = subject_data.get("chapters", {})
    if request.chapter_number not in chapters:
        max_chapter = max(chapters.keys())
        raise HTTPException(
            status_code=400,
            detail=f"Chapter {request.chapter_number} not found. Valid chapters for {request.subject} class {request.class_number}: 1–{max_chapter}"
        )

    # Build the prompt
    try:
        prompt = build_question_prompt(
            class_number=request.class_number,
            subject=request.subject,
            chapter_number=request.chapter_number,
            total_questions=request.total_questions,
            question_distribution=request.question_distribution or {},
            extra_instructions=request.extra_instructions or "",
            difficulty=request.difficulty or "mixed",
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    # Call Gemini
    try:
        result = generate_questions(prompt)
    except ValueError as e:
        raise HTTPException(status_code=502, detail=f"AI response parsing failed: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"AI service error: {str(e)}")

    return GenerateQuestionsResponse(
        request_id=str(uuid.uuid4()),
        status="success",
        data=result,
    )


async def handle_get_curriculum(class_number: int, subject: str):
    """Returns chapter list for a given class and subject."""
    subject = subject.lower().replace(" ", "_")
    if class_number not in VALID_CLASSES:
        raise HTTPException(status_code=400, detail=f"Class must be 9 or 10")
    if subject not in VALID_SUBJECTS:
        raise HTTPException(status_code=400, detail=f"Subject must be one of: {', '.join(VALID_SUBJECTS)}")

    subject_data = CURRICULUM[class_number][subject]
    chapters = {
        num: {"title": ch["title"], "unit": ch.get("unit"), "topics": ch["topics"]}
        for num, ch in subject_data["chapters"].items()
    }

    return {
        "class": class_number,
        "subject": subject_data["subject_full"],
        "total_chapters": len(chapters),
        "chapters": chapters,
    }


async def handle_generate_pdf(request: GenerateQuestionsRequest) -> dict:
    """Generates questions using AI and returns Question and Solution PDFs."""
    response = await handle_generate_questions(request)
    
    metadata = {
        "class": request.class_number,
        "subject": request.subject,
        "chapter": request.chapter_number
    }
    
    return {
        "questions": create_questions_pdf(response.data, metadata),
        "solutions": create_solutions_pdf(response.data, metadata)
    }