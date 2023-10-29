from sqlalchemy.orm import Session
from src.models.login import Login as LoginModel
from src.schemas.login import Login


def get_login(db: Session, username: str):
    return (
        db.query(LoginModel)
        .filter(LoginModel.username == username)
        .first()
    )

def get_logins(db: Session):
    return db.query(LoginModel).all()


def create_login(db: Session, login: Login):
    db_login = LoginModel(
        username=login.username,
        password=login.password,
    )
    db.add(db_login)
    db.commit()
    db.refresh(db_login)
    return db_login
