from fastapi import FastAPI
from . import database

app = FastAPI()
db = database.create_database()

@app.get("/")
def root():
    return "Hello World"


@app.get("/article/{id}")
def get_article_by_id(id: str):
    ...
    