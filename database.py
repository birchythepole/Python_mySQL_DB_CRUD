import mysql.connector
from env import env

db = mysql.connector.connect(**env)
cursor = db.cursor()