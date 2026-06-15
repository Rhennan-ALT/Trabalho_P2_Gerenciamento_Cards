from sqlalchemy.orm import Session
from .models import Carta
from .schemas import CartaPCreate

def criar_carta_poke(db: Session, card: CartaPCreate):
    db_card = Carta(**card.model_dump())
    db.add(db_card)
    db.commit()
    db.refresh(db_card)
    return db_card

def get_cartas_poke(db: Session):
    return db.query(Carta).all()

def get_carta_poke(db: Session, card_id: int):
    return db.query(Carta).filter(Carta.id == card_id).first()

def up_carta_poke(db: Session, card_id: int, card):
    db_card = get_carta_poke(db, card_id)
    if db_card:
        for key, value in card.model_dump().items():
            setattr(db_card, key, value)
        db.commit()
        db.refresh(db_card)
    return db_card

def del_carta_poke(db: Session, card_id: int):
    db_card = get_carta_poke(db, card_id)
    if db_card:
        db.delete(db_card)
        db.commit()
    return db_card