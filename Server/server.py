from fastapi import FastAPI
from app.api import auth, tsp
from app.db.base import Base
from app.db.session import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router, prefix="/api")
app.include_router(tsp.router, prefix="/api")