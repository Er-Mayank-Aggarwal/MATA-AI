import io
from fastapi import APIRouter, Depends, Query, Response, Body
from app.controllers.question_controller import (
    handle_generate_questions,
    handle_get_curriculum,
    GenerateQuestionsRequest,
    GenerateQuestionsResponse
)
from app.services.pdf_service import create_questions_pdf, create_solutions_pdf

router = APIRouter(prefix="/api/v1", tags=["Questions"])


@router.post("/questions/generate", response_model=GenerateQuestionsResponse)
async def generate_questions(request: GenerateQuestionsRequest):
    """Generate unique CBSE questions (JSON format for live preview)."""
    return await handle_generate_questions(request)


@router.post("/questions/download/questions")
async def download_questions_pdf(
    data: dict = Body(...),
    metadata: dict = Body(...)
):
    """Convert JSON data to Questions PDF."""
    pdf_content = create_questions_pdf(data, metadata)
    filename = f"Questions_{metadata.get('subject', 'CBSE')}_Class{metadata.get('class', '')}.pdf"
    return Response(
        content=pdf_content,
        media_type="application/pdf",
        headers={"Content-Disposition": f"attachment; filename={filename}"}
    )


@router.post("/questions/download/solutions")
async def download_solutions_pdf(
    data: dict = Body(...),
    metadata: dict = Body(...)
):
    """Convert JSON data to Solutions PDF."""
    pdf_content = create_solutions_pdf(data, metadata)
    filename = f"Solutions_{metadata.get('subject', 'CBSE')}_Class{metadata.get('class', '')}.pdf"
    return Response(
        content=pdf_content,
        media_type="application/pdf",
        headers={"Content-Disposition": f"attachment; filename={filename}"}
    )


@router.get("/curriculum/{class_number}/{subject}")
async def get_curriculum(class_number: int, subject: str):
    return await handle_get_curriculum(class_number, subject)