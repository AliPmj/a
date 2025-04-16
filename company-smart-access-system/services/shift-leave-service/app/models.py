from sqlalchemy import Table, Column, Integer, String, Date, Time, ForeignKey, Boolean
from app.database import metadata

shifts = Table(
    "shifts", metadata,
    Column("id", Integer, primary_key=True),
    Column("employee_id", Integer),
    Column("date", Date),
    Column("start_time", Time),
    Column("end_time", Time),
    Column("remote", Boolean, default=False),
)

leaves = Table(
    "leaves", metadata,
    Column("id", Integer, primary_key=True),
    Column("employee_id", Integer),
    Column("start_date", Date),
    Column("end_date", Date),
    Column("type", String),  # مرخصی، ماموریت
    Column("status", String, default="pending")  # approved/rejected
)
