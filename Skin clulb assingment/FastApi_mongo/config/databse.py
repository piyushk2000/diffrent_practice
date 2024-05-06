from pymongo import MongoClient



client = MongoClient('mongodb+srv://pk:piyupiyu@chatapp.gtnbm9i.mongodb.net/?retryWrites=true&w=majority')

db = client.test

userCollection = db["users"]