from motor.motor_asyncio import AsyncIOMotorClient


MONGO_DETAILS = "mongodb+srv://dtanwer:deepak123@cluster0.0qqm1l6.mongodb.net/?retryWrites=true&w=majority"
client =AsyncIOMotorClient(MONGO_DETAILS)
database = client.students
student_collection = database.get_collection("students")


def student_helper(student) -> dict:
    return {
        "id": str(student["_id"]),
        "fullname": student["fullname"],
        "email": student["email"],
        "password": student["password"],
        "year": student["year"],
        "GPA": student["gpa"],
    }
