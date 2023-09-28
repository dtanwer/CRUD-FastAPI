from fastapi import FastAPI
from app.server.routes.student import router as StudentRouter
from app.server.routes.auth import router as AuthRouter
app = FastAPI()

app.include_router(StudentRouter, tags=["Student"], prefix="/student")
app.include_router(AuthRouter, tags=["Auth"], prefix="/auth")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}