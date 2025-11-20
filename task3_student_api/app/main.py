from fastapi import FastAPI, Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from . import models, database
from .routers import students, groups

# 创建数据库表
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Student API", version="1.0.0")

# 包含路由
app.include_router(students.router)
app.include_router(groups.router)

@app.get("/")
def read_root():
    return {"message": "Student API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)