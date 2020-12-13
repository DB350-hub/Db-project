import sqlite3
import pandas as pd
conn = sqlite3.connect('Database.db')
def check(username):
    cur=conn.cursor()
    cur.execute("""SELECT user_id from login""")
    li  = cur.fetchall()
    df = pd.DataFrame(li,columns = ["ID"])
    for i in df ["ID"]:
        if i ==username:
            print("duplicate")
            return True
    return False
check("erh")
