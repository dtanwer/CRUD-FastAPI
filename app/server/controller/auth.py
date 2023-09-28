from app.server.database import (student_collection, student_helper)
from bson.objectid import ObjectId
from app.server.models.response import AuthResponseModel, ErrorResponseModel
from app.server.utils.hashPassword import  verify_password
from jose import jwt
import time
from typing import Dict

JWT_SECRET="secret"
JWT_ALGORITHM="HS256"

async def loginUser(student_data: dict)-> dict:
    student = await student_collection.find_one({"email": student_data.email})
    if not student:
        return ErrorResponseModel("An error occurred.", 404, "Student doesn't exist.")
    if not verify_password(student_data.password, student["password"]):
        return ErrorResponseModel("An error occurred.", 404, "Incorrect password.")  
    token = signJWT(str(student["_id"]))
    student["token"] = token
    return AuthResponseModel(student_helper(student), "Student retrieved successfully.", token )




def signJWT(user_id: str) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "expires": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    data=jwt.decode("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNjUxNTMwOGJiOTgxZjFiMGJmMzI2MmZhIiwiZXhwaXJlcyI6MTY5NTkwMTgwMy40OTk5NjZ9.LfR0YmOj3AIgVRIEARQvXBbUk_2cVKAi0nctXtiwWxQ", JWT_SECRET, algorithms=[JWT_ALGORITHM])
    print(data)

    return token_response(token)


def token_response(token: str):
    return {
        "access_token": token
    }