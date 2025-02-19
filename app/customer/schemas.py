
from sqlmodel import Field, Relationship, Session, SQLModel, select
from typing import Optional

class CustomerBase(SQLModel):
    name: str = Field(default=None)
    description: str | None = Field(default=None)
    price: int

# Modelo para crear una nueva tarea (hereda de TaskBase)
class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(CustomerBase):
    pass
