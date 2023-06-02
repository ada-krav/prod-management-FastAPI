import schemas, models
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter, Response
from database import get_db

router = APIRouter()

@router.get('/')
def get_products(db: Session = Depends(get_db), limit: int = 10, page: int = 1, search: str = ''):
    skip = (page - 1) * limit

    products = db.query(models.Product).filter(
        models.Product.name.contains(search)).limit(limit).offset(skip).all()
    return {'status': 'success', 'results': len(products), 'products': products}
