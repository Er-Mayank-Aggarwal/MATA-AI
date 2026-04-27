from fpdf import FPDF
import io

class QuestionPaperPDF(FPDF):
    def header(self):
        # Background color for header
        self.set_fill_color(240, 240, 240)
        self.rect(0, 0, 210, 30, 'F')
        
        self.set_font('helvetica', 'B', 16)
        self.set_text_color(44, 62, 80)
        self.cell(0, 20, 'CBSE QUESTION BANK', ln=True, align='C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica', 'I', 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

def sanitize_text(text: str) -> str:
    """Replaces common Unicode and Math characters with PDF-safe ASCII equivalents."""
    if not text:
        return ""
    replacements = {
        "\u2022": "-", "\u2026": "...", "\u201c": "\"", "\u201d": "\"",
        "\u2018": "'", "\u2019": "'", "\u2014": "--", "\u2013": "-",
        "\u2264": "<=", "\u2265": ">=", "\u221a": "sqrt", "\u03c0": "pi",
        "\u00b0": " deg", "\u00b1": "+/-",
    }
    for char, replacement in replacements.items():
        text = text.replace(char, replacement)
    return text.encode("latin-1", "replace").decode("latin-1")

def create_questions_pdf(data: dict, metadata: dict) -> bytes:
    pdf = QuestionPaperPDF()
    pdf.set_margins(15, 20, 15)
    pdf.add_page()
    effective_width = pdf.epw
    
    # Metadata Section
    pdf.set_font('helvetica', 'B', 12)
    pdf.set_fill_color(230, 230, 250)
    pdf.cell(effective_width, 10, f" Class: {metadata['class']} | Subject: {metadata['subject'].title()} ", ln=True, fill=True)
    pdf.cell(effective_width, 10, f" Chapter {metadata['chapter']}: {data.get('chapter_name', data.get('metadata', {}).get('chapter_title', 'Question Set'))} ", ln=True, fill=True)
    pdf.ln(5)

    # Questions
    pdf.set_font('helvetica', 'B', 14)
    pdf.set_text_color(192, 57, 43)
    pdf.cell(effective_width, 10, 'SECTION A: QUESTIONS', ln=True)
    pdf.set_text_color(0, 0, 0)
    pdf.ln(2)

    questions = data.get('questions', [])
    for i, q in enumerate(questions, 1):
        pdf.set_font('helvetica', 'B', 11)
        raw_type = q.get('type', 'General').lower()
        display_type = raw_type.replace('_', ' ').title()
        pdf.multi_cell(effective_width, 7, sanitize_text(f"Q{i}. [{display_type}] ({q.get('marks', 1)} Marks)"), ln=True)
        
        pdf.set_x(15)
        pdf.set_font('helvetica', '', 11)

        if "assertion" in raw_type:
            pdf.multi_cell(effective_width, 6, sanitize_text(f"Assertion (A): {q.get('assertion', '')}"), ln=True)
            pdf.set_x(15)
            pdf.multi_cell(effective_width, 6, sanitize_text(f"Reason (R): {q.get('reason', '')}"), ln=True)
        elif "case" in raw_type:
            pdf.set_font('helvetica', 'I', 11)
            pdf.multi_cell(effective_width, 6, sanitize_text(q.get('passage', '')), ln=True)
            pdf.ln(2)
            pdf.set_font('helvetica', '', 11)
            for j, sub in enumerate(q.get('sub_questions', []), 1):
                pdf.set_x(20)
                pdf.multi_cell(effective_width - 5, 6, sanitize_text(f"{j}) {sub.get('q', '')} ({sub.get('marks', 1)} Mark)"), ln=True)
        else:
            pdf.multi_cell(effective_width, 6, sanitize_text(q.get('question', '')), ln=True)
        
        options = q.get('options', {})
        if options and isinstance(options, dict) and (raw_type == "mcq" or "assertion" in raw_type):
            for key, val in options.items():
                pdf.set_x(25)
                pdf.multi_cell(effective_width - 10, 6, sanitize_text(f"{key}) {val}"), ln=True)
        pdf.ln(5)

    return bytes(pdf.output())

def create_solutions_pdf(data: dict, metadata: dict) -> bytes:
    pdf = QuestionPaperPDF()
    pdf.set_margins(15, 20, 15)
    pdf.add_page()
    effective_width = pdf.epw
    
    pdf.set_font('helvetica', 'B', 14)
    pdf.set_text_color(39, 174, 96)
    pdf.cell(effective_width, 10, 'ANSWER KEY & MARKING SCHEME', ln=True)
    pdf.set_text_color(0, 0, 0)
    pdf.ln(5)

    questions = data.get('questions', [])
    for i, q in enumerate(questions, 1):
        pdf.set_font('helvetica', 'B', 11)
        pdf.cell(effective_width, 7, f"Solution to Q{i}:", ln=True)
        pdf.set_x(15)
        pdf.set_font('helvetica', '', 11)
        
        q_type = q.get('type', '').lower()
        if "case" in q_type:
            for j, sub in enumerate(q.get('sub_questions', []), 1):
                pdf.set_x(20)
                pdf.multi_cell(effective_width - 5, 6, sanitize_text(f"{j}) {sub.get('answer', '')}"), ln=True)
        else:
            ans = q.get('correct_answer') or q.get('expected_answer') or q.get('answer', 'See below')
            pdf.multi_cell(effective_width, 6, sanitize_text(f"Correct Answer: {ans}"), ln=True)
        
        if q.get('explanation'):
            pdf.set_x(15)
            pdf.set_font('helvetica', 'I', 10)
            pdf.set_text_color(100, 100, 100)
            pdf.multi_cell(effective_width, 5, sanitize_text(f"Explanation: {q['explanation']}"), ln=True)
            pdf.set_text_color(0, 0, 0)
        pdf.ln(4)

    return bytes(pdf.output())
