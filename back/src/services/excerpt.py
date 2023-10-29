from io import BytesIO
from fastapi import UploadFile
from pandas import read_excel, DataFrame
from sqlalchemy.orm import Session
from src.services.classifier import classify_multiple_texts, classify_single_text
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


def get_excerpts_by_category(db: Session, category: int) -> List[ExcerptModel]:
    return (
        db.query(ExcerptModel)
        .filter(ExcerptModel.category == category)
        .all()
    )


def get_train_excerpts(db: Session) -> List[ExcerptModel]:
    return (
        db.query(ExcerptModel)
        .filter(ExcerptModel.test_or_train == 'train')
        .all()
    )


def get_test_excerpts(db: Session) -> List[ExcerptModel]:
    return (
        db.query(ExcerptModel)
        .filter(ExcerptModel.test_or_train == "test")
        .all()
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


def create_train_excerpts_from_excel(db: Session, file: UploadFile) -> (bool, str):
    df = read_excel(BytesIO(file.file.read()))

    if len(df.columns) != 2:
        return (False, "The dataframe must have exactly two columns")

    for _, row in df.iterrows():
        db_excerpt = ExcerptModel(
            id=str(uuid4()),
            text=row["Textos_espanol"],
            category=row["sdg"],
            test_or_train="train"
        )
        db.add(db_excerpt)
        db.commit()
        db.refresh(db_excerpt)

    return (True, "Train excerpts uploaded successfully")


def create_test_excerpts_from_excel(db: Session, file: UploadFile) -> (bool, str):
    df = read_excel(BytesIO(file.file.read()))

    if len(df.columns) != 2:
        return (False, "The dataframe must have exactly two columns")

    for _, row in df.iterrows():
        db_excerpt = ExcerptModel(
            id=str(uuid4()),
            text=row["Textos_espanol"],
            category=row["sdg"],
            test_or_train="test"
        )
        db.add(db_excerpt)
        db.commit()
        db.refresh(db_excerpt)

    return (True, "Test excerpts uploaded successfully")


def classify_text(text: str) -> int:
    return classify_single_text(text)


def create_excerpts(db: Session, excerpts: List[ExcerptCreate]) -> List[ExcerptModel]:
    return list(map(lambda excerpt: create_excerpt(db, excerpt), excerpts))


def create_excerpts_from_excel(db: Session, file: UploadFile) -> (bool, str):
    df = read_excel(BytesIO(file.file.read()))

    if len(df.columns) > 1:
        return (False, "The dataframe must have only one column")
    elif len(df.columns) < 1:
        return (False, "The dataframe must have at least one column")
    
    for index, row in df.iterrows():
        if get_excerpt_by_text(db, row[df.columns[0]]):
            df.drop(index=index, inplace=True)

    if df.empty:
        return (True, "All excerpts already exist in the database")

    answ_df = classify_multiple_texts(df)

    excerpts = []
    for _, row in answ_df.iterrows():
        db_excerpt = ExcerptModel(
            id=str(uuid4()),
            text=row[df.columns[0]],
            category=row["sdg"]
        )
        db.add(db_excerpt)
        db.commit()
        db.refresh(db_excerpt)
        excerpts.append(db_excerpt)

    return (True, "Excerpts created and classified successfully")


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
