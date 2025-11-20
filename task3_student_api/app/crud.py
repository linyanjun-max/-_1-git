from sqlalchemy.orm import Session
from sqlalchemy import and_
from . import models, schemas

# Student CRUD operations
def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()

def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Student).offset(skip).limit(limit).all()

def delete_student(db: Session, student_id: int):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if student:
        # 先删除与组的关系
        student.groups.clear()
        db.commit()
        db.delete(student)
        db.commit()
    return student

# Group CRUD operations
def create_group(db: Session, group: schemas.GroupCreate):
    db_group = models.Group(**group.dict())
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group

def get_group(db: Session, group_id: int):
    return db.query(models.Group).filter(models.Group.id == group_id).first()

def get_groups(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Group).offset(skip).limit(limit).all()

def delete_group(db: Session, group_id: int):
    group = db.query(models.Group).filter(models.Group.id == group_id).first()
    if group:
        # 先清空组内的学生关系
        group.students.clear()
        db.commit()
        db.delete(group)
        db.commit()
    return group

# Student-Group relationship operations
def add_student_to_group(db: Session, student_id: int, group_id: int):
    student = get_student(db, student_id)
    group = get_group(db, group_id)
    if student and group:
        # 检查是否已经存在关系
        if student not in group.students:
            group.students.append(student)
            db.commit()
    return group

def remove_student_from_group(db: Session, student_id: int, group_id: int):
    student = get_student(db, student_id)
    group = get_group(db, group_id)
    if student and group:
        # 直接操作关联表来删除关系
        delete_stmt = models.student_group.delete().where(
            and_(
                models.student_group.c.student_id == student_id,
                models.student_group.c.group_id == group_id
            )
        )
        db.execute(delete_stmt)
        db.commit()
    return group

def get_students_in_group(db: Session, group_id: int):
    group = db.query(models.Group).filter(models.Group.id == group_id).first()
    return group.students if group else []

def transfer_student(db: Session, student_id: int, from_group_id: int, to_group_id: int):
    try:
        # 先检查学生和组是否存在
        student = get_student(db, student_id)
        from_group = get_group(db, from_group_id)
        to_group = get_group(db, to_group_id)
        
        if not all([student, from_group, to_group]):
            return False
        
        # 检查学生是否在源组中
        if student not in from_group.students:
            return False
            
        # 移除学生从源组
        remove_student_from_group(db, student_id, from_group_id)
        
        # 添加学生到目标组
        add_student_to_group(db, student_id, to_group_id)
        
        return True
    except Exception as e:
        db.rollback()
        print(f"Transfer error: {e}")
        return False