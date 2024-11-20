from pymongo import MongoClient
from config import DATABASE_URI

client = MongoClient(DATABASE_URI)
db = client.mmo_bot

def save_character_data(user_id, data):
    db.characters.update_one({"user_id": user_id}, {"$set": data}, upsert=True)

def get_character_data(user_id):
    return db.characters.find_one({"user_id": user_id})
