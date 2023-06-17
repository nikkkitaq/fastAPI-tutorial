import sqlalchemy as sa
from sqlalchemy.orm import DeclarativeBase

metadata = sa.MetaData()


class BaseModel(DeclarativeBase):
    pass


class Users(BaseModel):
    __tablename__ = "users"
    metadata,
    id = sa.Column(sa.Integer, primary_key=True),
    username = sa.Column(sa.String(length=100), nullable=False),
    password = sa.Column(sa.String(length=100), nullable=False),
    permissions = sa.Column(sa.JSON)

