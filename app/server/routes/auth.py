from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.server.controller.auth import loginUser
from app.server.models.student import UpdateStudentModel

router = APIRouter()

@router.post("/login")
async def login(student_data:UpdateStudentModel):
    student = await loginUser(student_data)
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid credentials",
        )
    return student