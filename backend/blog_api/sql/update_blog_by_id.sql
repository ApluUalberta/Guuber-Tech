UPDATE blogs 
SET title = :title
    author = :author
    content = :content
    draft = :draft
    archived = :archived
WHERE id = :id