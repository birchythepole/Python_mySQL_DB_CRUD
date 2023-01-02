from env import logs
from database import cursor, db

def add_log(text,user):
    sql = ("INSERT INTO logs(text, user) VALUES (%s, %s)")
    cursor.execute(sql,(text,user,))
    db.commit()
    log_id = cursor.lastrowid
    print("Added log {}".format(log_id))

for l in logs:
        add_log(l['content'],l['user'])