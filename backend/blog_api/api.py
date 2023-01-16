from typing import List

from fastapi import FastAPI, HTTPException

from . import database, models, __version__

app = FastAPI(
    title="Guuber Tech",
    description="""Rest API for the blog. It is very minimal by design. 
    Please use with care. Contact Noah if you have and issues.""",
    version=__version__)

db = database.connect()

@app.get("/articles")
async def get_articles() -> List[models.Blog]:
    return db.get_all_blogs()


@app.post("/articles", status_code=201)
async def post_article(blog: models.Blog) -> None:
    return db.add_blog(blog)

@app.get("/articles/{id}")
async def get_article(id: str) -> models.Blog:
    try:
        return db.get_blog_by_id(id)
    except database.DatabaseException:
        raise HTTPException(status_code=404, detail="Blog not found.")

@app.patch("/articles/{id}", status_code=204)
async def update_article(id: str, blog: models.Blog):
    try:
        blog.id = id
        db.update_blog(id)
    except database.DatabaseException:
        raise HTTPException(status_code=404, detail="Blog not found.")

@app.delete("/articles/{id}", status_code=204)
async def delete_article(id: str):
    try:
        db.delete_blog_by_id(id)
    except database.DatabaseException:
        raise HTTPException(status_code=404, detail="Blog not found.")
