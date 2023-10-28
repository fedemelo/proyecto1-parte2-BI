from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.schemas.excerpt import ExcerptResponse, ExcerptCreate
import src.services.excerpt as service
from src.config.db_settings import get_db


router = APIRouter(
    prefix="/excerpts",
    tags=["excerpts"],
    responses={404: {"detail": "Not found"}},
)


@router.get("/{id}", response_model=ExcerptResponse, status_code=200)
def get_excerpt(id: str, db: Session = Depends(get_db)) -> ExcerptResponse:
    db_excerpt = service.get_excerpt(db, id)
    if db_excerpt is None:
        raise HTTPException(
            status_code=404, detail=f"Excerpt with id {id} not found")
    return db_excerpt


@router.get("/", response_model=List[ExcerptResponse], status_code=200)
def get_excerpts(db: Session = Depends(get_db)) -> List[ExcerptResponse]:
    return service.get_excerpts(db)


@router.post("/", response_model=ExcerptResponse, status_code=201)
def create_excerpt(excerpt: ExcerptCreate, db: Session = Depends(get_db)) -> ExcerptResponse:
    db_excerpt = service.get_excerpt_by_text(db, excerpt.text)
    if db_excerpt:
        raise HTTPException(
            status_code=400, detail="Duplicate excerpt: An excerpt with the given text already exists")
    return service.create_excerpt(db=db, excerpt=excerpt)


@router.post("/many", response_model=List[ExcerptResponse], status_code=201)
def create_excerpts(excerpts: List[ExcerptCreate], db: Session = Depends(get_db)) -> List[ExcerptResponse]:
    return list(map(lambda excerpt: create_excerpt(excerpt, db), excerpts))


@router.put("/{id}", response_model=ExcerptResponse, status_code=200)
def update_excerpt(id: str, excerpt: ExcerptCreate, db: Session = Depends(get_db)) -> None:
    get_excerpt(id=id, db=db)  # Check if the excerpt exists
    return service.update_excerpt(db=db, id=id, excerpt=excerpt)


@router.delete("/{id}", status_code=204)
def delete_excerpt(id: str, db: Session = Depends(get_db)) -> None:
    get_excerpt(id=id, db=db)  # Check if the excerpt exists
    return service.delete_excerpt(db=db, id=id)