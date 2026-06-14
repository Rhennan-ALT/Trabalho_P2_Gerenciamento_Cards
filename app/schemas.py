from pydantic import BaseModel

class CartaPBase(BaseModel):
    nome: str
    tipo: str
    hp: int
    rar: str
    desc: str

class CartaPCreate(CartaPBase):
    pass

class CartaPoke(CartaPBase):
    id: int
    
    class Config:
        from_attributes = True