from  datetime import date
from pydantic import BaseModel, ConfigDict,SkipValidation , EmailStr ,conint , validator  
from typing import Optional  , List


class UserBase(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    password: str
    type: str  # "student" or "teacher"

    @validator('type')
    def validate_type(cls, v):
        if v not in ['student', 'teacher']:
            raise ValueError("type must be either 'student' or 'teacher'")
        return v


    

class StudentCreate(UserBase):
    sap_id : int 
    department: str
    roll_no: str
    graduation_year: Optional[int]
    gpa: Optional[float]

    @validator('gpa')
    def validate_gpa(cls, v):
        if v is not None and (v < 0.0 or v > 10.0):
            raise ValueError('GPA must be between 0.0 and 10.0')
        return v
    


class TeacherCreate(UserBase):
    teacher_id : int 
    department: str
    start_date: date


class TeacherOut(BaseModel):
    id: int
    teacher_id: int
    first_name :str 
    last_name :str
    email: EmailStr
    type: str
    department: str
    start_date: date

    model_config = {
        "from_attributes": True
    }



class StudentOut(BaseModel):
    id: int
    sap_id: int
    type: str
    department: str
    email : EmailStr 
    first_name :str
    last_name :str
    roll_no: str
    graduation_year: Optional[int]
    gpa: Optional[float]

    model_config = {
        "from_attributes": True
    }

class Token(BaseModel):
    access_token: str
    token_type: str



class TokenData(BaseModel):
    id: Optional[str] = None

    