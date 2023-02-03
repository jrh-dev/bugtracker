from sqlalchemy.orm import Session
from api import models, schemas


def get_user(db: Session, user_id: int) -> list[tuple]:
    """ return record for single specified user """
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100) -> list[tuple]:
    """ return records for all users """
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserBase):
    """ add a record for a new user """
    db_tmp = models.User(first=user.first, last=user.last)
    db.add(db_tmp)
    db.commit()
    db.refresh(db_tmp)
    return db_tmp


def get_bug(db: Session, bug_id: int) -> list[tuple]:
    """ return record for single specified bug """
    return db.query(models.Bug).filter(models.Bug.id == bug_id).first()


def get_bugs(db: Session, skip: int = 0, limit: int = 100) -> list[tuple]:
    """ return records for all bugs """
    return db.query(models.Bug).offset(skip).limit(limit).all()


def create_bug(db: Session, bug: schemas.BugBase, user_id: int):
    """ add a record for a new bug """
    db_tmp = models.Bug(
        title=bug.title,
        description=bug.description,
        is_open=True,
        owner_id=user_id
    )
    db.add(db_tmp)
    db.commit()
    db.refresh(db_tmp)
    return db_tmp
