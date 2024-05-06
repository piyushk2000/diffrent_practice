from fastapi import APIRouter
# from models.todos import Show
from config.databse import  userCollection
from schema.schemas import user_serial
from bson import ObjectId


router = APIRouter()

@router.get("/active_users")
async def get_active_users():
    users_cursor = userCollection.find({"isActive": True})
    users = [user_serial(user) for user in users_cursor]
    return users

@router.get("/users")
async def get_all_users():
    users_cursor = userCollection.find()
    users = [user_serial(user) for user in users_cursor]
    return users
