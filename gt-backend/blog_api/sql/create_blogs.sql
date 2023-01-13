CREATE TABLE IF NOT EXISTS blogs (
    id INTEGER PRIMARY KEY,
    author TEXT NOT NULL, 
    date_created DATETIME NOT NULL,
    title TEXT NOT NULL,
    content TEXT,
    draft TEXT,
    archived BOOL
)