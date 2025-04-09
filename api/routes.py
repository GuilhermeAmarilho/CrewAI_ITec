from fastapi import APIRouter, Query
from api.controller import get_artigo

router = APIRouter()

@router.get("/artigo")
# a variavel topic sera string e vira via get
def artigo(topic: str = Query(..., description="Tema do artigo")):
    return get_artigo(topic)