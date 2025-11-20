from sqlalchemy.orm import Session
from ..models.user import User, LoginHistory
from ..schemas.user import UserCreate, UserUpdate
from ..auth.security import get_password_hash, verify_password

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user_update: UserUpdate):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return None
    
    update_data = user_update.dict(exclude_unset=True)
    if "password" in update_data:
        update_data["hashed_password"] = get_password_hash(update_data.pop("password"))
    
    for field, value in update_data.items():
        setattr(db_user, field, value)
    
    db.commit()
    db.refresh(db_user)
    return db_user

def add_login_history(db: Session, user_id: int, user_agent: str = None):
    login_record = LoginHistory(user_id=user_id, user_agent=user_agent)
    db.add(login_record)
    db.commit()
    return login_record

def get_login_history(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(LoginHistory).filter(LoginHistory.user_id == user_id)\
        .offset(skip).limit(limit).all()