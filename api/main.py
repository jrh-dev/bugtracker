from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from api import crud, models, schemas
from api.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    """ create new session on request and closes on completion """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def index():
    return {"title": "simple bug tracker"}

@app.post("/users/create/", response_model=schemas.UserBase)
async def create_user(user: schemas.UserBase, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)


@app.patch("/users/update/{user_id}", response_model=schemas.UserUpdate)
async def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = user.dict(exclude_unset=True)
    for key, value in user_data.items():
        setattr(db_user, key, value)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.get("/users/", response_model=list[schemas.UserGet])
def get_all_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.UserGet)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/bugs/create/{user_id}", response_model=schemas.BugBase)
def create_bug(user_id: int, bug: schemas.BugBase, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.create_bug(db=db, bug=bug, user_id=user_id)


@app.patch("/bugs/update/{bug_id}", response_model=schemas.BugUpdate)
def update_bug(bug_id: int, bug: schemas.BugUpdate, db: Session = Depends(get_db)):
    db_bug = crud.get_bug(db, bug_id=bug_id)
    if db_bug is None:
        raise HTTPException(status_code=404, detail="Bug not found")
    bug_data = bug.dict(exclude_unset=True)
    for key, value in bug_data.items():
        setattr(db_bug, key, value)
    db.add(db_bug)
    db.commit()
    db.refresh(db_bug)
    return db_bug


@app.get("/bugs/", response_model=list[schemas.BugGet])
def get_all_bugs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    bugs = crud.get_bugs(db, skip=skip, limit=limit)
    return bugs


@app.get("/bugs/{bug_id}", response_model=schemas.BugGet)
def get_bug(bug_id: int, db: Session = Depends(get_db)):
    db_bug = crud.get_bug(db, bug_id=bug_id)
    if db_bug is None:
        raise HTTPException(status_code=404, detail="Bug not found")
    return db_bug
