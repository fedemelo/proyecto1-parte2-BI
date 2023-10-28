from sqlalchemy.orm import Session
from src.models.excerpt import Excerpt as ExcerptModel
from src.schemas.excerpt import ExcerptCreate, ExcerptResponse
from typing import List
from uuid import uuid4


def get_excerpt(db: Session, id: str) -> ExcerptModel:
    return (
        db.query(ExcerptModel)
        .filter(ExcerptModel.id == id)
        .first()
    )


def get_excerpt_by_text(db: Session, text: str) -> ExcerptModel:
    return (
        db.query(ExcerptModel)
        .filter(ExcerptModel.text == text)
        .first()
    )


def get_excerpts(db: Session) -> List[ExcerptModel]:
    return db.query(ExcerptModel).all()


def create_excerpt(db: Session, excerpt: ExcerptCreate) -> ExcerptModel:
    db_excerpt = ExcerptModel(
        id=str(uuid4()),
        text=excerpt.text,
        category=classify_text(excerpt.text)
    )
    db.add(db_excerpt)
    db.commit()
    db.refresh(db_excerpt)
    return db_excerpt


def classify_text(text: str) -> int:
    # TODO
    return 16


def create_excerpts(db: Session, excerpts: List[ExcerptCreate]) -> List[ExcerptModel]:
    return list(map(lambda excerpt: create_excerpt(db, excerpt), excerpts))


def update_excerpt(db: Session, id: str, excerpt: ExcerptResponse) -> ExcerptModel:
    db_excerpt = get_excerpt(db, id)
    db_excerpt.id = excerpt.id
    db_excerpt.text = excerpt.text
    db_excerpt.category = excerpt.category
    db.commit()
    db.refresh(db_excerpt)
    return db_excerpt


def delete_excerpt(db: Session, id: str) -> None:
    db_excerpt = get_excerpt(db, id)
    db.delete(db_excerpt)
    db.commit()
