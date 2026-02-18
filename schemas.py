from pydantic import BaseModel
from datetime import datetime

class EmployeeCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    department: str

class AttendanceCreate(BaseModel):
    employee_id: int
    check_type: str
    device_id: str | None = None
