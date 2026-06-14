from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import Base, engine, SessionLocal
from . import crud, schemas

Base.metadata.create_all(bind=engine)
app = FastAPI(title= "API Cartas Pokémon")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/cartas", response_model=schemas.CartaPoke)
def criar_card(
    card: schemas.CartaPCreate, 
    db: Session = Depends(get_db)
):
    return crud.criar_carta_poke(db, card)

@app.get("/cartas", response_model=list[schemas.CartaPoke])
def get_cards(
    db: Session=Depends(get_db)
):
    return crud.get_cartas_poke(db)

@app.get("/cartas/{card_id}", response_model=schemas.CartaPoke)
def get_card(card_id: int, db: Session = Depends(get_db)):
    
    card = crud.get_carta_poke(db, card_id)
    if not card:
        raise HTTPException(status_code=404, detail="Essa Carta não foi Encontrada...")
    return card

@app.put("/cartas/{card_id}", response_model=schemas.CartaPoke)
def up_card(card_id: int, card: schemas.CartaPCreate, db: Session=Depends(get_db)):
    
    upado = crud.up_carta_poke(db, card_id, card)
    if not upado:
        raise HTTPException(status_code=404, detail= "Essa Carta não foi Encontrada")
    return upado

@app.delete("/cartas/{card_id}")
def del_card(card_id: int, db: Session=Depends(get_db)):
    
    deletado = crud.del_carta_poke(db, card_id)
    if not deletado:
        raise HTTPException(status_code=404, detail= "Essa Carta não foi Encontrada")
    return {"message": "Essa Carta foi Deletada..."}

