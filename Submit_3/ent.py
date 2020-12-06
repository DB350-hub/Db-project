from tkinter import *
from tkinter import messagebox
import time
from buy import *
from mainpg import *
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
# from tkinter.ttk import *
# from login import loginWindow
import sqlite3
conn = sqlite3.connect('Database.db')

root = Tk()
user_id = ''
ID = Entry(root, width= 50)
ID.pack()
PW = Entry(root, width= 50)
PW.pack()
EM=Entry(root, width=50)
EM.pack()
def mon_e(app):
    money= Entry(app, width= 50)
    money.pack()
    return money

def username_password (conn,username,password):
    print(username,password,"io")
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

def Login():
    username = ID.get()
    password = PW.get()
    user_id = username
    UID = Label(root, text = username)
    UID.pack()
    UPass = Label(root, text = password)
    UID.pack()
    # myButton = Button(root, text = "Submit", command = Login)
    # myButton.pack()
    validate(username,password)
    main_page(user_id)

def Signup():
    username = ID.get()
    user_id = username
    email=EM.get()
    password = PW.get()
    UID = Label(root, text = username)
    UID.pack()
    UEmail = Label(root, text = email)
    UID.pack()
    UPass = Label(root, text = password)
    UID.pack()

    # myButton = Button(root, text = "Submit", command = Signup)
    # myButton.pack()
    cur=conn.cursor()
    data= (username, password, email)
    cur.execute("""INSERT into login values (?,?,?)""", data)
    conn.commit()
    ask_money(user_id)


def validate(username,password):
    c = username
    p = password
    print(c,p)
    try:
        if (username_password(conn,c,p)):
         messagebox.showinfo("Successful", "Login Was Successful")
        else:
         messagebox.showerror("Error", "Wrong Credentials")
    except IndexError:
         messagebox.showerror("Error", "Wrong Credentials")

def ask_money(user_id):
    money = askstring('money', 'What is your starting balance?')
    showinfo('Hello!', 'youe balance is: {}'.format(money))
    UserMoney(conn, user_id, money)
    main_page(user_id)
def main_page(user_id):
    main_window(user_id)



def window():
    root.title("Bullstocks")
    root.geometry("800x500")
    root.config(bg="#FFE01B")
    cur = conn.cursor()
    label = Label(root, text="Login/Signup",font='lato')
    label.pack()
    login = Button(root, text="Submit")
    login.pack()
    register = Button(root, text="Signup",command=Signup)
    register.pack()

# submit = Button(root, text="Submit",pady=5, padx=20)
# submit.pack()


#root.mainloop()
def run():
    mainloop()

window()
run()
