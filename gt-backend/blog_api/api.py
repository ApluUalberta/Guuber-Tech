from typing import List

from fastapi import FastAPI

from . import database, models

app = FastAPI()
db = database.connect()

@app.get("/articles")
async def get_articles() -> List[models.Blog]:
    return db.get_all_blogs()


@app.post("/articles")
async def post_new_article(blog: models.Blog):
    db.add_blog(blog)

@app.post()
 

    