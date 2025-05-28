from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.sc import create_access_token, verify_password
from app.cruds.user import get_user, create_user
from app.db.session import get_db
from app.schemas.auth import UserCreate, User

router = APIRouter()

@router.post("/sign-up/", response_model=User)
def sign_up(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    user_data = user.dict()
    created_user = create_user(db, user_data)
    token = create_access_token(data={"sub": user.email})
    return {"id": created_user.id, "email": created_user.email, "token": token}

@router.post("/login/", response_model=User)
def login(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user(db, email=user.email)
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    token = create_access_token(data={"sub": user.email})
    return {"id": db_user.id, "email": db_user.email, "token": token}