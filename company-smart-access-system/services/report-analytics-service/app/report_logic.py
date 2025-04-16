import pandas as pd
from io import BytesIO
from reportlab.pdfgen import canvas

def generate_attendance_report(data):
    df = pd.DataFrame(data)
    output = BytesIO()
    df.to_excel(output, index=False)
    output.seek(0)
    return output

def generate_pdf_summary(title, rows):
    buffer = BytesIO()
    c = canvas.Canvas(buffer)
    c.drawString(100, 800, title)
    y = 750
    for row in rows:
        c.drawString(100, y, str(row))
        y -= 20
    c.save()
    buffer.seek(0)
    return buffer
