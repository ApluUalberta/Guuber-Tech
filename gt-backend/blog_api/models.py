from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

class Blog(BaseModel):
    id: Optional[int] = None
    date_created: datetime = Field(default_factory=datetime.now)
    archived: bool = False
    title: str
    author: str
    content: str
    draft: str
