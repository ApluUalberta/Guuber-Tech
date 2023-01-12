import sqlite3 as sql
from pathlib import Path


DB_PATH = Path("guuber.db")
SQL_COMMANDS_PATH = Path(__file__).parent / "sql"

def create_database():
    """Returns a database connection."""
    conn = sql.connect(str(DB_PATH))
    cur = conn.cursor()
    cur.execute(get_sql_string("create_blogs"))
    return conn

def get_sql_string(name):
    path = SQL_COMMANDS_PATH / f"{name}.sql"
    return path.read_text()
        
    