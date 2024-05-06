from bson import ObjectId

def user_serial(user) -> dict:
    return {
        "name": user["name"],
        "email": user["email"],
        "role": user["role"],
        "isActive": user["isActive"], 
    }
