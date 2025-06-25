from fastapi import FastAPI
from app.routes import router
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="UniForum - Moderation Service")
app.include_router(router, prefix="/reports", tags=["Moderation Reports"])
