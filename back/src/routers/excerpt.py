from typing import List
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from src.schemas.excerpt import ExcerptResponse, ExcerptCreate, ExcerptLog
import src.services.excerpt as service
from src.config.db_settings import get_db


router = APIRouter(
    prefix="/excerpts",
    tags=["excerpts"],
    responses={404: {"detail": "Not found"}},
)


@router.get("/train", response_model=List[ExcerptResponse], status_code=200)
def get_train_excerpts(db: Session = Depends(get_db)) -> List[ExcerptResponse]:
    return service.get_train_excerpts(db)


@router.get("/test", response_model=List[ExcerptResponse], status_code=200)
def get_test_excerpts(db: Session = Depends(get_db)) -> List[ExcerptResponse]:
    return service.get_test_excerpts(db)


@router.get("/log", response_model=List[ExcerptLog], status_code=200)
def get_log(db: Session = Depends(get_db)) -> List[ExcerptLog]:
    return service.get_real_life(db)


@router.get("/ods/{category}", response_model=List[ExcerptResponse], status_code=200)
def get_excerpt_by_category(category: int, db: Session = Depends(get_db)) -> ExcerptResponse:
    if not (category == 6 or category == 7 or category == 16):
        raise HTTPException(
            status_code=404, detail=f"The model can only classify categories 6, 7 and 16")
    return service.get_excerpts_by_category(db, category)


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


@router.post("/train", status_code=201)
def add_train_excerpts_from_excel(db: Session = Depends(get_db), file: UploadFile = File(...)) -> str:
    if (
        file.content_type
        != "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    ):
        raise HTTPException(
            400, detail="Invalid document type. Document must be an Excel file.")
    result = service.create_train_excerpts_from_excel(db=db, file=file)
    if not result[0]:
        raise HTTPException(400, detail=result[1])

    return result[1]


@router.post("/test", status_code=201)
def add_test_excerpts_from_excel(db: Session = Depends(get_db), file: UploadFile = File(...)) -> str:
    if (
        file.content_type
        != "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    ):
        raise HTTPException(
            400, detail="Invalid document type. Document must be an Excel file.")
    result = service.create_test_excerpts_from_excel(db=db, file=file)
    if not result[0]:
        raise HTTPException(400, detail=result[1])

    return result[1]


@router.post("/", response_model=ExcerptResponse, status_code=201)
def classify_excerpt(excerpt: ExcerptCreate, db: Session = Depends(get_db)) -> ExcerptResponse:
    db_excerpt = service.get_excerpt_by_text(db, excerpt.text)
    if db_excerpt:
        return db_excerpt
    return service.create_excerpt(db=db, excerpt=excerpt)


@router.post("/many", response_model=List[ExcerptResponse], status_code=201)
def classify_excerpts(excerpts: List[ExcerptCreate], db: Session = Depends(get_db)) -> List[ExcerptResponse]:
    return list(map(lambda excerpt: classify_excerpt(excerpt, db), excerpts))


@router.post("/excel", status_code=201)
def classify_excerpts_from_excel(db: Session = Depends(get_db), file: UploadFile = File(...)) -> str:
    if (
        file.content_type
        != "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    ):
        raise HTTPException(
            400, detail="Invalid document type. Document must be an Excel file.")
    result = service.create_excerpts_from_excel(db=db, file=file)
    if not result[0]:
        raise HTTPException(400, detail=result[1])

    return result[1]


@router.put("/{id}", response_model=ExcerptResponse, status_code=200)
def update_excerpt(id: str, excerpt: ExcerptCreate, db: Session = Depends(get_db)) -> None:
    get_excerpt(id=id, db=db)  # Check if the excerpt exists
    return service.update_excerpt(db=db, id=id, excerpt=excerpt)


@router.delete("/{id}", status_code=204)
def delete_excerpt(id: str, db: Session = Depends(get_db)) -> None:
    get_excerpt(id=id, db=db)  # Check if the excerpt exists
    return service.delete_excerpt(db=db, id=id)
