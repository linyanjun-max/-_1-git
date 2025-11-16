from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas, database

router = APIRouter(prefix="/groups", tags=["groups"])

@router.post("/", response_model=schemas.Group)
def create_group(group: schemas.GroupCreate, db: Session = Depends(database.get_db)):
    return crud.create_group(db=db, group=group)

@router.get("/{group_id}", response_model=schemas.Group)
def read_group(group_id: int, db: Session = Depends(database.get_db)):
    db_group = crud.get_group(db, group_id=group_id)
    if db_group is None:
        raise HTTPException(status_code=404, detail="Group not found")
    return db_group

@router.get("/", response_model=List[schemas.Group])
def read_groups(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    groups = crud.get_groups(db, skip=skip, limit=limit)
    return groups

@router.delete("/{group_id}")
def delete_group(group_id: int, db: Session = Depends(database.get_db)):
    db_group = crud.delete_group(db, group_id=group_id)
    if db_group is None:
        raise HTTPException(status_code=404, detail="Group not found")
    return {"message": "Group deleted successfully"}

@router.post("/{group_id}/students/{student_id}")
def add_student_to_group(group_id: int, student_id: int, db: Session = Depends(database.get_db)):
    result = crud.add_student_to_group(db, student_id=student_id, group_id=group_id)
    if not result:
        raise HTTPException(status_code=404, detail="Student or Group not found")
    return {"message": "Student added to group successfully"}

@router.delete("/{group_id}/students/{student_id}")
def remove_student_from_group(group_id: int, student_id: int, db: Session = Depends(database.get_db)):
    result = crud.remove_student_from_group(db, student_id=student_id, group_id=group_id)
    if not result:
        raise HTTPException(status_code=404, detail="Student or Group not found")
    return {"message": "Student removed from group successfully"}

@router.get("/{group_id}/students", response_model=List[schemas.Student])
def get_students_in_group(group_id: int, db: Session = Depends(database.get_db)):
    students = crud.get_students_in_group(db, group_id=group_id)
    return students

@router.post("/transfer")
def transfer_student(transfer: schemas.StudentTransfer, db: Session = Depends(database.get_db)):
    result = crud.transfer_student(
        db, 
        student_id=transfer.student_id,
        from_group_id=transfer.from_group_id,
        to_group_id=transfer.to_group_id
    )
    if not result:
        raise HTTPException(status_code=404, detail="Student or Groups not found")
    return {"message": "Student transferred successfully"}