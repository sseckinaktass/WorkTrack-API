from sqlalchemy.orm import Session
import models, schemas

def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = models.Employee(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def create_attendance(db: Session, attendance: schemas.AttendanceCreate):
    db_attendance = models.AttendanceLog(**attendance.dict())
    db.add(db_attendance)
    db.commit()
    db.refresh(db_attendance)
    return db_attendance
