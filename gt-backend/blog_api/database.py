__all__ = ["connect"]

import sqlite3
import datetime
import os
from pathlib import Path

from . import sql, config, models
    
def adapt_datetime_iso(val):
    """Adapt datetime.date to ISO 8601 date."""
    return val.isoformat()

def convert_datetime(val):
    """Convert ISO 8601 datetime to datetime.datetime object."""
    return datetime.datetime.fromisoformat(val.decode())

def adapt_bool(val):
    """Adapt a bool into an integer."""
    return int(val)

def convert_bool(val):
    """Convert an integer back to a boolean."""
    return bool(val.decode())

def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}

sqlite3.register_adapter(datetime.datetime, adapt_datetime_iso)
sqlite3.register_adapter(bool, adapt_bool)
sqlite3.register_converter("bool", convert_bool)
sqlite3.register_converter("datetime", convert_datetime)

def initialize():
    """Create the tables in the blog"""
    with sqlite3.connect(str(config.DB_PATH)) as conn:
        conn.execute(sql.commands.create_blogs)

def delete():
    """Deletes the database"""
    if config.DB_PATH.exists():
        os.remove(config.DB_PATH)
        

class DB:
    def __init__(self):
        if not config.DB_PATH.exists():
            initialize()
        self.conn = sqlite3.connect(
            str(config.DB_PATH), detect_types=sqlite3.PARSE_DECLTYPES
        )
        self.conn.row_factory = dict_factory

    def add_blog(self, blog: models.Blog):
        with self.conn:
            self.conn.execute(sql.commands.add_blog, blog.dict())
    
    def get_all_blogs(self):
        with self.conn:
            query = self.conn.execute(sql.commands.fetch_all_blogs)
            return [models.Blog(**q) for q in query.fetchall()]

    def get_blog_by_id(self, id_: int):
        with self.conn:
            query = self.conn.execute(sql.commands.fetch_blog_by_id, (id_,))
            return models.Blog(**query.fetchone())

    def delete_blog_by_id(self, id_: int)
        with self.conn:
            self.conn.execute(sql.commands.delete_blog_by_id, (id_,))

    def update_blog(self, blog: models.blog):
        with self.conn:
            self.conn.execute(sql.commands.update_blog_by_id, blog.dict())

    def get_title_to_id_dict(self):
        with self.conn:
            query = self.conn.execute(sql.commands.fetch_title_and_id)
            return dict(query.fetchall())




def connect():
    """Returns a database object."""
    return DB()
    