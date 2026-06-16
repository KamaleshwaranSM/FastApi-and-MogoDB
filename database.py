from pymongo import MongoClient
from urllib.parse import quote_plus
username = "Admin"
password = quote_plus("your password")
client=MongoClient(f"mongodb+srv://{username}:{password}@cluster0.x0mb8wb.mongodb.net/?appName=Cluster0")

db=client.todo_db

collection_name=db["todo_collection"]
