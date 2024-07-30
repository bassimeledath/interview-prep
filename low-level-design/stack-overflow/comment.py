from pydantic import BaseModel
from datetime import datetime


class Comment(BaseModel):
    comment_id: int
    timestep: str
    user_id: int
    text: str

    @classmethod
    def create(cls, comment_id: int, user_id: int, text: str):
        return cls(
            comment_id=comment_id,
            timestep=datetime.now().isoformat(),
            user_id=user_id,
            text=text
        )
