CREATE TABLE IF NOT EXISTS blogs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    author TEXT NOT NULL, 
    date_created DATE,
    content TEXT,
    draft TEXT,
    deleted INTEGER
)