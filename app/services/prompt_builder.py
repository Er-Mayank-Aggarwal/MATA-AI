from app.constants.curriculum import CURRICULUM, QUESTION_TYPES
from app.constants.grounding import GROUNDING_DATA


def build_question_prompt(
    class_number: int,
    subject: str,
    chapter_number: int,
    total_questions: int,
    question_distribution: dict,
    extra_instructions: str = "",
    difficulty: str = "mixed",
) -> str:
    subject_data = CURRICULUM[class_number][subject]
    chapter = subject_data["chapters"].get(chapter_number)

    if not chapter:
        raise ValueError(f"Chapter {chapter_number} not found for {subject} class {class_number}")

    topics_text = ", ".join(chapter["topics"])
    unit_text = f" (Unit: {chapter['unit']})" if "unit" in chapter else ""
    distribution_text = _format_distribution(question_distribution, total_questions)
    difficulty_text = _format_difficulty(difficulty)

    # Fetch grounding focus points (chapter-specific)
    focus_points = GROUNDING_DATA.get(class_number, {}).get(subject, {}).get(chapter_number, [])
    focus_text = "\n".join([f"  - {point}" for point in focus_points]) if focus_points else "  - Use general CBSE standards for this subject."

    prompt = f"""You are a senior CBSE question paper setter with 15+ years of experience designing board exam papers for Class {class_number}.

## STEP 0 — CBSE PYQ GROUNDING (Crucial)
To ensure the questions are not random and are highly relevant to actual board exams, prioritize these recurring themes and high-weightage concepts for this subject/class:
{focus_text}

## TASK
Generate exactly {total_questions} high-quality questions for:
- **Class:** {class_number}  
- **Subject:** {subject_data['subject_full']}
- **Chapter {chapter_number}:** {chapter['title']}{unit_text}
- **Key Topics Covered:** {topics_text}
- **Difficulty Mix:** {difficulty_text}

---

## STEP 1 — ANALYZE BEFORE GENERATING (Critical)
Before writing any question, recall from your training knowledge and the **PYQ GROUNDING** focus points in Step 0:
1. The pattern of CBSE board questions asked from this chapter in past 5–10 years.
2. Which topics from this chapter are most frequently tested (Prioritize the points in Step 0).
3. Common student mistakes and misconceptions in this chapter.
4. The exact language and phrasing style used in CBSE official question papers.
5. The weightage of this chapter in the CBSE marking scheme.

Use all of the above analysis to ensure your questions are exam-realistic and follow CBSE standards precisely.

---

## STEP 2 — QUESTION DISTRIBUTION
Generate questions in this exact distribution:
{distribution_text}

---

## STEP 3 — QUALITY STANDARDS (Strictly follow)
- **UNIFORMITY & VARIETY:** Every question must be unique. If you generate multiple questions for the same topic (e.g., 'Redox'), ensure they test different sub-concepts (e.g., oxidizing agents vs. balancing a redox equation) or different application levels (e.g., direct definition vs. identifying redox in a real-life scenario).
- **NO CROSS-TYPE DUPLICATION:** Do NOT ask the same question in different formats. For example, if you ask for the definition of 'Corrosion' in a Short Answer, do NOT make 'Corrosion' the main focus of a Long Answer.
- **COMPETENCY-BASED:** Focus on 'how' and 'why' rather than just 'what'. Use 'Imagine', 'Predict', 'Identify the error', or 'Analyze the observation' style phrasing where possible.
- **CBSE Standard:** Every question must be unambiguous and have a definitive correct answer.
- **MCQs:** all 4 options must be plausible; distractors should test real misconceptions.
- **Assertion-Reason:** test understanding of causality; avoid simple factual combinations.
- **Language:** clear, standard CBSE English — no ambiguity.
- **SYLLABUS COMPLIANCE:** Use the provided topics as the scope. You MAY use your internal knowledge of sub-topics, examples, and reactions that fall naturally under these broad topics, as long as they are part of the standard Class {class_number} CBSE syllabus.
- Spread questions across ALL topics listed above to ensure full chapter coverage.

---

## STEP 4 — ADDITIONAL INSTRUCTIONS FROM USER
{extra_instructions if extra_instructions.strip() else "No additional instructions provided."}

---

## OUTPUT FORMAT (Strict JSON — no markdown, no extra text)
Return a valid JSON object with this exact structure:

{{
  "metadata": {{
    "class": {class_number},
    "subject": "{subject_data['subject_full']}",
    "chapter_number": {chapter_number},
    "chapter_title": "{chapter['title']}",
    "total_questions": {total_questions},
    "difficulty": "{difficulty}"
  }},
  "questions": [
    {{
      "question_number": 1,
      "type": "mcq",
      "question": "Question text here",
      "options": {{
        "A": "Option A",
        "B": "Option B",
        "C": "Option C",
        "D": "Option D"
      }},
      "correct_answer": "A",
      "explanation": "Why A is correct and others are wrong",
      "topic": "Specific topic from chapter",
      "difficulty": "easy|medium|hard",
      "marks": 1
    }},
    {{
      "question_number": 2,
      "type": "assertion_reason",
      "assertion": "Assertion text",
      "reason": "Reason text",
      "options": {{
        "A": "Both Assertion and Reason are true and Reason is the correct explanation of Assertion",
        "B": "Both Assertion and Reason are true but Reason is NOT the correct explanation of Assertion",
        "C": "Assertion is true but Reason is false",
        "D": "Assertion is false but Reason is true"
      }},
      "correct_answer": "A",
      "explanation": "Detailed explanation",
      "topic": "Specific topic",
      "difficulty": "medium",
      "marks": 1
    }},
    {{
      "question_number": 3,
      "type": "short_answer",
      "question": "Question text",
      "expected_answer": "Model answer with key points",
      "marks": 3,
      "topic": "Specific topic",
      "difficulty": "medium"
    }},
    {{
      "question_number": 4,
      "type": "long_answer",
      "question": "Question text",
      "expected_answer": "Detailed model answer with all key points",
      "marks": 5,
      "topic": "Specific topic",
      "difficulty": "hard"
    }},
    {{
      "question_number": 5,
      "type": "case_study",
      "passage": "The case study passage text here",
      "sub_questions": [
        {{"q": "Sub question 1", "answer": "Answer 1", "marks": 1}},
        {{"q": "Sub question 2", "answer": "Answer 2", "marks": 1}},
        {{"q": "Sub question 3", "answer": "Answer 3", "marks": 2}}
      ],
      "total_marks": 4,
      "topic": "Specific topic",
      "difficulty": "medium"
    }}
  ]
}}

Only return valid JSON. No markdown. No explanation outside the JSON. Start your response with {{ and end with }}.
"""
    return prompt


def _format_distribution(distribution: dict, total: int) -> str:
    if not distribution:
        return f"  - Distribute {total} questions as you see fit based on CBSE exam pattern for this chapter"

    lines = []
    provided_total = sum(distribution.values())
    for q_type, count in distribution.items():
        type_label = QUESTION_TYPES.get(q_type, q_type.replace("_", " ").title())
        lines.append(f"  - {type_label}: {count} questions")

    if provided_total != total:
        lines.append(f"\n  ⚠️ Note: Distribution sums to {provided_total} but total_questions is {total}. Adjust proportionally to reach exactly {total} questions.")

    return "\n".join(lines)


def _format_difficulty(difficulty: str) -> str:
    presets = {
        "easy": "Easy (80% easy, 15% medium, 5% hard)",
        "medium": "Medium (20% easy, 60% medium, 20% hard)",
        "hard": "Hard (10% easy, 30% medium, 60% hard)",
        "mixed": "Mixed — CBSE standard (30% easy, 50% medium, 20% hard)",
        "board_exam": "Board Exam Pattern (25% easy, 50% medium, 25% hard)",
    }
    return presets.get(difficulty.lower(), difficulty)