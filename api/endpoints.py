import logging
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from api import crud, models, schemas
from api.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()


def get_db():
    """ create new session on request and closes on completion """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
async def index():
    return {"title": "simple bug tracker"}


@router.post("/users/create/", response_model=schemas.UserBase)
async def create_user(user: schemas.UserBase, db: Session = Depends(get_db)):
    logging.info(f'Start create_user: {user}')
    res = crud.DBI.create_user(db=db, user=user)
    logging.info(f'create_user complete: {user}')
    return res


@router.patch("/users/update/{user_id}", response_model=schemas.UserUpdate)
async def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    logging.info(f'Start update_user: {user_id}')
    db_user = crud.DBI.get_user(db, user_id=user_id)
    logging.info(f'Checking user exists: {user_id}')
    if db_user is None:
        logging.info(f'User not found - {user_id}')
        raise HTTPException(status_code=404, detail="User not found")
    user_data = user.dict(exclude_unset=True)
    for key, value in user_data.items():
        setattr(db_user, key, value)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    logging.info(f'update_user complete: user {user_id} - {user}')
    return db_user


@router.get("/users/", response_model=list[schemas.UserGet])
def get_all_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    logging.info(f'Start get_all_users')
    users = crud.DBI.get_users(db, skip=skip, limit=limit)
    logging.info(f'get_all_users complete: {len(users)} users found')
    return users


@router.get("/users/{user_id}", response_model=schemas.UserGet)
def get_user(user_id: int, db: Session = Depends(get_db)):
    logging.info(f'Start get_user - {user_id}')
    db_user = crud.DBI.get_user(db, user_id=user_id)
    logging.info(f'Checking user exists - {user_id}')
    if db_user is None:
        logging.info(f'User not found - {user_id}')
        raise HTTPException(status_code=404, detail="User not found")
    logging.info(f'get_user complete: user {user_id} returned')
    return db_user


@router.post("/bugs/create/{user_id}", response_model=schemas.BugBase)
def create_bug(user_id: int, bug: schemas.BugBase, db: Session = Depends(get_db)):
    logging.info(f'Start create_bug - {user_id}')
    db_user = crud.DBI.get_user(db, user_id=user_id)
    logging.info(f'Checking assigned user exists - {user_id}')
    if db_user is None:
        logging.info(f'User not found - {user_id}')
        raise HTTPException(status_code=404, detail="User not found")
    db_bug = crud.DBI.create_bug(db=db, bug=bug, user_id=user_id)
    logging.info(f'create_bug complete: {bug}')
    return db_bug


@router.patch("/bugs/update/{bug_id}", response_model=schemas.BugUpdate)
def update_bug(bug_id: int, bug: schemas.BugUpdate, db: Session = Depends(get_db)):
    logging.info(f'Start update_bug: {bug_id}')
    db_bug = crud.DBI.get_bug(db, bug_id=bug_id)
    logging.info(f'Checking bug exists - {bug_id}')
    if db_bug is None:
        logging.info(f'Bug not found - {bug_id}')
        raise HTTPException(status_code=404, detail="Bug not found")
    bug_data = bug.dict(exclude_unset=True)
    for key, value in bug_data.items():
        setattr(db_bug, key, value)
    db.add(db_bug)
    db.commit()
    db.refresh(db_bug)
    logging.info(f'update_bug complete: bug {bug_id} - {bug}')
    return db_bug


@router.get("/bugs/", response_model=list[schemas.BugGet])
def get_all_bugs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    logging.info(f'Start get_all_bugs')
    bugs = crud.DBI.get_bugs(db, skip=skip, limit=limit)
    logging.info(f'get_all_bugs complete: {len(bugs)} bugs found')
    return bugs


@router.get("/bugs/{bug_id}", response_model=schemas.BugGet)
def get_bug(bug_id: int, db: Session = Depends(get_db)):
    logging.info(f'Start get_bug- {bug_id}')
    db_bug = crud.DBI.get_bug(db, bug_id=bug_id)
    logging.info(f'Checking bug exists - {bug_id}')
    if db_bug is None:
        logging.info(f'Bug not found - {bug_id}')
        raise HTTPException(status_code=404, detail="Bug not found")
    logging.info(f'get_bug complete: bug {bug_id} returned')
    return db_bug
