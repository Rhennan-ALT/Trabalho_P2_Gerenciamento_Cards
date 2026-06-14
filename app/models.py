from sqlalchemy import Column, Integer, String
from .database import Base

class Carta(Base):
    __tablename__ = "carta_pokemon"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    tipo = Column(String, nullable=False)
    hp = Column(Integer, nullable=False)
    rar = Column(String, nullable=False)
    desc = Column(String)