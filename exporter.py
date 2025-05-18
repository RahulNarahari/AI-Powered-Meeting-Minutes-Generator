from fpdf import FPDF

def export_to_pdf(transcript, summary, keywords, sentiment, output_file="minutes.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.multi_cell(0, 10, "Meeting Transcript:\n" + transcript[:2000])
    pdf.ln(10)
    pdf.multi_cell(0, 10, "Summary:\n" + summary)
    pdf.ln(10)
    pdf.multi_cell(0, 10, "Keywords: " + ", ".join(keywords))
    pdf.ln(10)
    pdf.multi_cell(0, 10, f"Sentiment: {sentiment}")

    pdf.output(output_file)