def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }
    
def AuthResponseModel(data, message,token):
    return {
        "data": [data],
        "code": 200,
        "token": token,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}