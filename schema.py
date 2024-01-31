from typing import Optional

from pydantic import BaseModel


class todobase(BaseModel):
    title: str
    description: Optional[str] = None


class todo_list_add(todobase):
    title: str
    description: str

    class Config:
        orm_mode = True


class todo_list(todo_list_add):
    id: int

    class Confige:
        orm_mode = True


class Update_todo_list(BaseModel):
    title: str
    description: Optional[str] = None

    class Config:
        orm_mode = True


class log_in(BaseModel):
    email: str
    password: str

    class Config:
        orm_mode = True


class work_to_done(BaseModel):
    work_topic: str
    working_hr: int

    class Config:
        orm_mode = True
