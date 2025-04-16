from fastapi import APIRouter, Response
from app.database import database
from app.report_logic import generate_attendance_report, generate_pdf_summary
from sqlalchemy import text

router = APIRouter()

@router.get("/attendance/excel")
async def attendance_excel():
    query = text("SELECT * FROM attendance")
    data = await database.fetch_all(query)
    file = generate_attendance_report([dict(row) for row in data])
    return Response(file.read(), media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

@router.get("/attendance/pdf")
async def attendance_pdf():
    query = text("SELECT * FROM attendance LIMIT 10")
    data = await database.fetch_all(query)
    file = generate_pdf_summary("Attendance Summary", [dict(row) for row in data])
    return Response(file.read(), media_type="application/pdf")
