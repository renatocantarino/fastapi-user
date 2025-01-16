from sqlalchemy.orm import Session
from .models import User
from .schemas import UserCreate



def get_users(db:Session):
    return db.query(User).all()

def get_user(db: Session, id: int):
    return db.query(User).filter(User.id == id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserCreate):   
    usr = User(name= user.name, email= user.email) 
    db.add(usr)
    db.commit()
    db.refresh(usr)
    return usr

def delete_user(db: Session, user_id: int):    
    db.delete(get_user(user_id))
    db.commit()