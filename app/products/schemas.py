
from sqlmodel import Field, Relationship, Session, SQLModel, select
from typing import Optional

class ProductBase(SQLModel):
    name: str = Field(default=None)
    description: str | None = Field(default=None)
    price: int

# Modelo para crear una nueva tarea (hereda de TaskBase)
class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass
