# backend/api/funding.py
from fastapi import APIRouter

router = APIRouter(
    prefix="/funding",
    tags=["funding"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def read_root():
    return {"Hello": "World"}