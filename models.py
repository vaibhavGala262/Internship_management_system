from sqlalchemy import TIMESTAMP, Column , String ,Boolean, Integer, text , ForeignKey  , Float  , Date
from sqlalchemy.orm import relationship
from database import Base 




class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(256), nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False  , server_default=text('now()'))
    type = Column(String(50))  # Add this to User class

    __mapper_args__ = {
        "polymorphic_identity": "user",
        "polymorphic_on": type,
        "with_polymorphic": "*"
    }

    
    
class Student(User):
    __tablename__ = "students"
    sap_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    department= Column(String(50)  , nullable = False )
    roll_no = Column(String(50) , nullable = False ,unique = True)
    graduation_year = Column(Integer , nullable = True )
    gpa = Column(Float , nullable = True )

    __mapper_args__ = {
        "polymorphic_identity": "student"
    }


class Teacher(User):
    __tablename__ = "teachers"
    teacher_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    department = Column(String(50) , nullable = False )
    start_date = Column(Date, nullable = False )  # e.g., 2024-04-07

    __mapper_args__ = {
        "polymorphic_identity": "teacher",
    }

    