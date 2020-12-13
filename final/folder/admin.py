import sqlite3
conn = sqlite3.connect('Database.db')
cur =  conn.cursor()
data = ("admin","admin",None)
cur.execute(""" INSERT into Login values (?,?,?)""",data)
conn.commit()
