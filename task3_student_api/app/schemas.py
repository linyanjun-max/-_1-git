from pydantic import BaseModel
from typing import List, Optional

class StudentBase(BaseModel):
    name: str
    email: str

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int

    class Config:
        from_attributes = True

class GroupBase(BaseModel):
    name: str
    description: Optional[str] = None

class GroupCreate(GroupBase):
    pass

class Group(GroupBase):
    id: int

    class Config:
        from_attributes = True

class StudentGroupUpdate(BaseModel):
    student_id: int
    group_id: int

class StudentTransfer(BaseModel):
    student_id: int
    from_group_id: int
    to_group_id: int