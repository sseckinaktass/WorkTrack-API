from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, crud
from database import engine, SessionLocal
import schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/employees/")
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db, employee)


@app.post("/attendance/")
def create_attendance(attendance: schemas.AttendanceCreate, db: Session = Depends(get_db)):
    return crud.create_attendance(db, attendance)
