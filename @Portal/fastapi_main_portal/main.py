from fastapi import FastAPI , HTTPException , Depends , status
from pydantic import BaseModel
# from pydantic_settings import BaseSettings
from typing import List , Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from models import Student , Section , Subject , Teacher , Teaching , Studies
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from fastapi_jwt_auth import AuthJWT
# from fastapi_jwt_auth.exceptions import AuthJWTException

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

db_depedency = Annotated[Session , Depends(get_db)]

# class Settings(BaseSettings):
#     authjwt_secret_key: str = "secret"

# @AuthJWT.load_config
# def get_config():
#     return Settings()



# @app.post('/login')
# def login(user: OAuth2PasswordRequestForm = Depends(), Authorize: AuthJWT = Depends()):
#     if user.username != "test" or user.password != "test":
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Bad username or password")

#     access_token = Authorize.create_access_token(subject=user.username)
#     Authorize.set_access_cookies(access_token)
#     return {"msg": "Successfully login"}

# @app.get('/protected')
# def protected(Authorize: AuthJWT = Depends()):
#     Authorize.jwt_required()

#     current_user = Authorize.get_jwt_subject()
#     return {"logged_in_as": current_user}

# @app.post("/students/")
# def create_student(student: Student, Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
#     Authorize.jwt_required()

#     db_student = Student(name=student.name, section_id=student.section_id)
#     db.add(db_student)
#     db.commit()
#     db.refresh(db_student)
#     return db_student

class StudentBase(BaseModel):
    name: str
    section_id: int

class SectionBase(BaseModel):
    name: str

class SubjectBase(BaseModel):
    name: str

class TeacherBase(BaseModel):
    name: str

class StudiesBase(BaseModel):
    student_id: int
    subject_id: int

class TeachingBase(BaseModel):
    teacher_id: int
    subject_id: int
    section_id: int

@app.post("/students/")
def create_student(student: StudentBase, db: Session = Depends(get_db)):
    db_student = Student(name=student.name, section_id=student.section_id)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@app.post("/sections/")
def create_section(section: SectionBase, db: Session = Depends(get_db)):
    db_section = Section(name=section.name)
    db.add(db_section)
    db.commit()
    db.refresh(db_section)
    return db_section

@app.post("/subjects/")
def create_subject(subject: SubjectBase, db: Session = Depends(get_db)):
    db_subject = Subject(name=subject.name)
    db.add(db_subject)
    db.commit()
    db.refresh(db_subject)
    return db_subject

@app.post("/teachers/")
def create_teacher(teacher: TeacherBase, db: Session = Depends(get_db)):
    db_teacher = Teacher(name=teacher.name)
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher

@app.post("/studies/")
def create_studies(studies: StudiesBase, db: Session = Depends(get_db)):
    db_studies = Studies(student_id=studies.student_id, subject_id=studies.subject_id)
    db.add(db_studies)
    db.commit()
    db.refresh(db_studies)
    return db_studies

@app.post("/teachings/")
def create_teaching(teaching: TeachingBase, db: Session = Depends(get_db)):
    db_teaching = Teaching(teacher_id=teaching.teacher_id, subject_id=teaching.subject_id, section_id=teaching.section_id)
    db.add(db_teaching)
    db.commit()
    db.refresh(db_teaching)
    return db_teaching


# @app.post("/student/")
# async def create_student()

@app.get("/student/{student_id}")
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.get("/students/subject/{subject_name}")
def get_students_by_subject(subject_name: str, db: Session = Depends(get_db)):
    students = db.query(Student).join(Studies).join(Subject).filter(Subject.name == subject_name).all()
    return students

@app.get("/teachers/section/{section_id}")
def get_teachers_by_section(section_id: int, db: Session = Depends(get_db)):
    teachers = db.query(Teacher).join(Teaching).filter(Teaching.section_id == section_id).all()
    return teachers

######### GET ALL ####################

@app.get("/students/")
def get_all_students(db: Session = Depends(get_db)):
    students = db.query(Student).all()
    return students

@app.get("/sections/")
def get_all_sections(db: Session = Depends(get_db)):
    sections = db.query(Section).all()
    return sections

@app.get("/subjects/")
def get_all_subjects(db: Session = Depends(get_db)):
    subjects = db.query(Subject).all()
    return subjects

@app.get("/teachers/")
def get_all_teachers(db: Session = Depends(get_db)):
    teachers = db.query(Teacher).all()
    return teachers

@app.get("/studies/")
def get_all_studies(db: Session = Depends(get_db)):
    studies = db.query(Studies).all()
    return studies

@app.get("/teachings/")
def get_all_teachings(db: Session = Depends(get_db)):
    teachings = db.query(Teaching).all()
    return teachings