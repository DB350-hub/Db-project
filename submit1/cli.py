import sqlite3
conn = sqlite3.connect('Database.db')
cur = conn.cursor()

def username_password (conn,username,password):
    cur = conn.cursor()
    cur.execute("SELECT user_id FROM login")
    id = cur.fetchall()
    cur.execute("SELECT password FROM login")
    password_db = cur.fetchall()
    flagid = False
    flagpass = False
    for x in id:
        x =  ''.join(x)
        if(x ==username):
            flagid =True
    for x in password_db:
        x =  ''.join(x)
        if(x ==password):
            flagpass = True
    if flagid and flagpass == True:
        return True
    else:
        return False

def signup_db(conn,username,password,email):
    print(username,password,email,"i")
    try:
        cur = conn.cursor()
        data = (username,password,email)
        cur.execute("""INSERT into login values(?,?,?)""",data)
        conn.commit()
        return True
    except:
        print("Error")
        return False

print("Press 1 for login")
print("Press 2 to signup")
m = input("your choice:")
if(m =='1'):
    id= input("input id:")
    password= input("input password:")
    flag = username_password(conn,id,password)
    if(flag):
        print("Login successful")
    else:
        while(flag== False):
            print("try Again")
            id= input("input id:")
            password= input("input password:")
            flag = username_password(conn,id,password)
elif(m =='2'):
    print("Signup")
    id= input("input id:")
    password= input("input password:")
    email= input("input email:")
    flag = signup_db(conn,id,password,email)
    if(flag):
        print("successful")
    else:
        while(flag== False):
            print("try Again")
            id= input("input id:")
            password= input("input password:")
            email= input("input email:")
            flag = signup_db(conn,id,password,email)
else:
    print("Error")
