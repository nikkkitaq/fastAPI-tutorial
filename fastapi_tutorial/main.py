from fastapi import FastAPI, Query, Path
from pydantic import BaseModel
from typing import Annotated


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.get("/items/")
async def create_item(q: Annotated[list[str] | None, Query()] = None):
    query_items = {"q": q}
    return query_items
