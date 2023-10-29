from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.schemas.login import Login
from src.services import login as service
from src.config.db_settings import get_db


router = APIRouter(
    prefix="/logins",
    tags=["logins"],
    responses={404: {"detail": "Not found"}},
)


@router.get("/", response_model=List[Login], status_code=200)
def get_logins(db: Session = Depends(get_db)):
    return service.get_logins(db)


@router.get("/{username}", response_model=Login, status_code=200)
def get_login(username: str, db: Session = Depends(get_db)):
    db_login = service.get_login(db, username)
    if not db_login:
        raise HTTPException(status_code=404, detail="Login not found")
    return db_login


@router.post("/", status_code=201)
def check_login(login: Login, db: Session = Depends(get_db)):
    db_login = service.get_login(db, login.username)
    if not db_login:
        raise HTTPException(status_code=404, detail="Login not found")
    return {"username": db_login.username}
    
    
@router.post("/create", response_model=Login, status_code=201)
def create_login(login: Login, db: Session = Depends(get_db)):
    db_login = service.get_login(db, login.username)
    if db_login:
        raise HTTPException(status_code=400, detail="Login already exists")
    return service.create_login(db, login)