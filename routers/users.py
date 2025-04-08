from fastapi import FastAPI, Depends, HTTPException , APIRouter , status 
from sqlalchemy.exc import IntegrityError
from schemas import UserBase , TeacherCreate , StudentCreate  , TeacherOut , StudentOut
from database import get_db
from sqlalchemy.orm import Session
from utils import hash
import models
from typing import Union , List
from oauth import get_current_user , create_access_token , verify_access_token


router = APIRouter(
    prefix= "/users"  , 
    tags = ["Users"]
)


@router.get('/' ,response_model = List[StudentOut | TeacherOut] , status_code = 200)
def get_users( db: Session= Depends(get_db) ,  current_user:int= Depends(get_current_user)):
    cur_type= current_user.type
    if cur_type =='student':
        users = db.query(models.Teacher).all()
    elif cur_type=='teacher':
        users = db.query(models.Student).all()

    return users

@router.post('/' , status_code = 201 , response_model = TeacherOut |  StudentOut )
def post_users(user_data :  Union[StudentCreate, TeacherCreate] , db: Session = Depends(get_db)):
    if user_data.type =="student": 
        new_user=models.Student(
            email = user_data.email, 
            password= hash(user_data.password) ,
            first_name = user_data.first_name , 
            last_name = user_data.last_name ,
            department= user_data.department , 
            roll_no = user_data.roll_no , 
            graduation_year= user_data.graduation_year , 
            gpa = user_data.gpa, 
            type = user_data.type 

        )

    elif user_data.type=="teacher":
        new_user = models.Teacher(
            email = user_data.email , 
            password= hash(user_data.password) , 
            first_name = user_data.first_name  , 
            last_name = user_data.last_name , 
            department  =user_data.department , 
            start_date = user_data.start_date ,
            type = user_data.type 
        )


    else:
        raise HTTPException(status_code=400, detail="Invalid user type.")
    db.add(new_user)
    try:
        db.commit()
        db.refresh(new_user)
        return new_user
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with this email already exists"
        )
    

# update main teacher can change teacher details n student can change student but not interchange
@router.delete('/{id}' , status_code = 202)
def delete(id :int , db: Session = Depends(get_db) , current_user:int= Depends(get_current_user)):

    user= db.query(models.User).filter(models.User.id== id)
    if not user.first() : 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f'User with id {id} not found')
    
    if user.first().id != current_user.id :
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN , detail=f'not allowed to delete user with id {id}')
    
    
    print(user)
    user.delete(synchronize_session=False)
    db.commit()
    return {'detail' : f'post with id {id} deleted'}


# delete main teacher can delete teacher but student can delete student 



