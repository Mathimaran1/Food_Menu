import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
DATABASE_NAME = os.getenv("DATABASE_NAME", "foodmenu")

client = MongoClient(MONGO_URL)
db = client[DATABASE_NAME]

menu_collection = db["menu"]
category_collection = db["categories"]