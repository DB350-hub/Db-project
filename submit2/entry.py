from tkinter import *
from tkinter import messagebox
import time
# from login import loginWindow
import sqlite3
conn = sqlite3.connect('Database.db')

root = Tk()

ID = Entry(root, width= 50)
ID.pack()
PW = Entry(root, width= 50)
PW.pack()

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
	UID = Label(root, text = username)
	UID.pack()
	UPass = Label(root, text = password)
	UID.pack()
	print (username)
	print(password)
	# myButton = Button(root, text = "Submit", command = Login)
	# myButton.pack()
	validate(username,password)

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
    # if (c and p):
    #     print("found")
    # else:
    #     print("not found")

def window():
    # roo = Tk()
    root.title("Bullstocks")
    root.geometry("800x500")

    label = Label(root, text="Login/Signup")
    label.place(x=95, y=40)
    login = Button(root, text="Submit",pady=5, padx=30, command = Login)
    login.pack()
    register = Button(root, text="Signup",pady=5, padx=20)
    register.pack()

# submit = Button(root, text="Submit",pady=5, padx=20)
# submit.pack()


#root.mainloop()
def run():
    mainloop()
# cur = conn.cursor()
# data = ("aamina","123w","aami@gmail.com")
# cur.execute("""INSERT into login values(?,?,?)""",data)

window()
run()
