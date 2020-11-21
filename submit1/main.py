from tkinter import *
import time
from tkinter import messagebox
# from login import loginWindow
import sqlite3
conn = sqlite3.connect('Database.db')
clicked =False
usr =''
passw = ''
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
def signup_db(conn,username,password,email):
    print(usr,passw,email,"i")
    try:
        cur = conn.cursor()
        data = (username,password,email)
        cur.execute("""INSERT into login values(?,?,?)""",data)
    except:
        print("Error")
def clk():
    print("in")
    clicked =True
    if clicked ==True:
        print(usr,passw)
        validate(usr,passw)


def validate(username,password):
    # c= username_password(conn,username,password)
    print(username,password,"b")
    messagebox.showinfo('Message', 'You clicked the Submit button!')
    # if (c):
    #     print("found")
    # else:
    #     print("not found")
def window():
    app = Tk()
    app.title("Bullstocks")
    app.geometry("800x500")
    label = Label(app, text="Login/Signup")
    label.place(x=95, y=40)
    login = Button(app, text="Login",pady=5, padx=30,command = loginWindow)
    login.place(x=100, y=100)
    register = Button(app, text="Signup",pady=5, padx=20, command=signup)
    register.place(x=100, y=150)


def loginWindow():
    loginWindow1 = Tk()
    loginWindow1.title("login")
    loginWindow1.geometry("800x500")
    label = Label(loginWindow1, text="Login/Signup")
    label.place(x=95, y=40)
    usernamei = StringVar()
    passwordi = StringVar()
    username = Entry(loginWindow1, relief=FLAT, textvariable=usernamei)
    username.place(x=70, y=80)
    password = Entry(loginWindow1, relief=FLAT, textvariable=passwordi)
    password.place(x=70, y=120)

    username = usernamei.get()
    password = passwordi.get()
    print(username,password)
    usr =username
    passw =password
    submit =  Button(loginWindow1, text="Submit",pady=5, padx=20,command=clk)
    submit.place(x=100, y=150)

    # submit['command'] = clk()

def signup():
    loginWindow = Tk()
    loginWindow.title("Bullstocks")
    loginWindow.geometry("800x500")
    label = Label(loginWindow, text="Login/Signup")
    label.place(x=95, y=40)
    usernamei = StringVar()
    passwordi = StringVar()
    emaili = StringVar()
    username = Entry(loginWindow, relief=FLAT, textvariable=usernamei)
    username.place(x=70, y=80)
    password = Entry(loginWindow, relief=FLAT, textvariable=passwordi)
    password.place(x=70, y=120)
    email = Entry(loginWindow, relief=FLAT, textvariable=emaili)
    email.place(x=70, y=160)
    username = usernamei.get()
    password = passwordi.get()
    email= emaili.get()
    submit =  Button(loginWindow, text="Submit",pady=5, padx=20)
    submit.place(x=150, y=200)
    signup_db(conn,username,password,email)

def run():
    mainloop()
# def register():
#     registerTk = Register()
#     registerTk.run()

# loginWindow()
window()
run()
# root = tk.Tk()
# gui = MainWindow(root)
# gui.pack()
# root.mainloop()
