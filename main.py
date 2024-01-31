from email.header import Header
from ensurepip import version
from turtle import title
from typing import List

from fastapi import Depends, FastAPI, Header, HTTPException
from sqlalchemy.orm import Session

import crud
import model
import schema
from database import SessionLocal, engine

model.Base.metadata.create_all(bind=engine)


app = FastAPI(title="Todos_List", descption="you can perform crud ", version="1.0.0")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/todos", response_model=List[schema.todo_list])
def list_of_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    todo = crud.get_todo(db=db, skip=skip, limit=limit)
    return todo


@app.get("/todos/{id}")
def return_a_todo(id: int, db: Session = Depends(get_db)):
    todo = crud.get_todo_by_id(db=db, id=id)
    if not todo:
        raise HTTPException(status_code=404, detail=f"No record found")
    return todo


@app.post("/log_in", response_model=schema.log_in)
def log_in(log_in: schema.log_in, db: Session = Depends(get_db)):
    return crud.user_log_in(db=db, log_in=log_in)


@app.post("/to_do", response_model=schema.work_to_done)
def get_to_do(
    to_do: schema.work_to_done, email: str = Header(None), db: Session = Depends(get_db)
):
    return crud.user_to_do(to_do=to_do, db=db, email=email)


@app.get("/logins", response_model=List[schema.log_in])
def list_of_logins(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    log_in = crud.get_log_in_usres(db=db, skip=skip, limit=limit)
    return log_in


@app.post("/todos", response_model=schema.todo_list_add)
def new_todo(todo: schema.todo_list_add, db: Session = Depends(get_db)):
    # title = crud.get_todo_by_todo_id(db=db, title=model.todo_list.title)
    # if title:
    #     raise HTTPException(status_code=400, detail=f"Movie id {model.todo_list.title} already exist in database: {title}")
    return crud.add_todo_details_to_db(db=db, todo=todo)


@app.delete("/todos/{id}")
def delete_todo_by_id(id: int, db: Session = Depends(get_db)):
    details = crud.get_todo_by_id(db=db, id=id)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to delete")

    try:
        crud.delete_todo_details_by_id(db=db, sl_id=id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to delete: {e}")
    return {"delete status": "success"}


@app.put("/todos/{id}", response_model=schema.todo_list)
def update_a_todo(
    id: int, update_param: schema.Update_todo_list, db: Session = Depends(get_db)
):
    details = crud.get_todo_by_id(db=db, id=id)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to update")

    return crud.update_todo_details(db=db, details=update_param, sl_id=id)
