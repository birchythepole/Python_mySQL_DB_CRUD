from env import logs
from database import cursor, db

#Add Logs
def add_log(text,user):
    sql = (f"INSERT INTO logs(text, user) VALUES ({text}, {user})")
    cursor.execute(sql)
    db.commit()
    log_id = cursor.lastrowid
    print("Added log {}".format(log_id))

# Get all logs
def get_logs(sortColumn):
    sql = (f"SELECT * FROM logs ORDER BY {sortColumn} DESC")
    cursor.execute(sql)
    result = cursor.fetchall()

    for row in result:
        print(row)

# Get single specyfic log
def get_log(id):
    sql = (f"SELECT * FROM logs WHERE id = {id}")
    cursor.execute(sql)
    result = cursor.fetchone()

    for row in result:
        print(row)

# Update Log

def update_log(id,text):
    sql = ("UPDATE logs SET text = %s WHERE id = %s")
    cursor.execute(sql,(text,id,))
    db.commit()
    print("Log updated")

#Delete Log
def delete_log(id):
    sql = ("DELETE FROM logs WHERE id = %s")
    cursor.execute(sql,(id,))
    db.commit()
    print("Log Deleted")


# Inserting Logs into DataBase, you need in your env.py file a list called 
# logs with dictionaries as items, with structure {content,user}
# for l in logs:
#         add_log(logs,l['content'],l['user'])

#get_logs('logs','created')
#get_log('logs',1)
#update_log(2,'replace')
#delete_log(2)