import mysql.connector
from env import user

db = mysql.connector.connect(**user)
cursor = db.cursor()