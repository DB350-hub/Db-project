from tkinter import *
from tkinter import messagebox
import time
from buy import *
from mainpg import *
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo,askretrycancel
# from tkinter.ttk import *
# from login import loginWindow
import sqlite3
conn = sqlite3.connect('Database.db')

root = Tk()
# user_id = ''
C = Canvas(root,bg="#FA5F1A", height=250, width=300)
filename = PhotoImage(file = "Asset 2final.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()
ID = Entry(root, width= 25)
ID.place(x= 400,y =15)
PW = Entry(root, width= 20)
PW.place(x= 400,y =40)
EM=Entry(root, width=20)
EM.place(x= 400,y =80)
data = ("admin","admin",None)
cur =conn.cursor()
cur.execute(""" INSERT into Login values (?,?,?)""",data)
conn.commit()

def mon_e(app):
    money= Entry(app, width= 50)
    money.pack()
    return money

def username_password (conn,username,password):
    print(username,password,"io")
    cur = conn.cursor()
    cur.execute("SELECT user_id FROM login")
    id = cur.fetchall()
    cur.execute("""SELECT password FROM login where user_id = ?""",(username,))
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
            print(password ,x ,"pass,x")
            flagpass = True
    if flagid and flagpass == True:
        return True
    else:
        return False

def Login():
    username = ID.get()
    password = PW.get()
    user_id = username
    UID = Label(root, text = "username")

    UPass = Label(root, text = "password")

    # myButton = Button(root, text = "Submit", command = Login)
    # myButton.pack()

    a = validate(username,password)
    if a:
        main_page(username)
    else:
        askretrycancel(title = "retry",message = "retry or Cancel")
        ID.delete(0,'end')
        PW.delete(0,'end')
        username = ID.get()
        password = PW.get()
        user_id = username

def Signup():
    username = ID.get()
    user_id = username
    email=EM.get()
    password = PW.get()
    UID = Label(root, text = username)

    UEmail = Label(root, text = email)

    UPass = Label(root, text = password)


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

    # if check(username, password):
    #     cur=conn.cursor()
    #     data= (username, password, email)
    #     cur.execute("""INSERT into login values (?,?,?)""", data)
    #     conn.commit()
    if check(username):
            askretrycancel(title = "retry",message = "retry or Cancel")
            ID.delete(0,'end')
            PW.delete(0,'end')
            username = ID.get()
            password = PW.get()
            user_id = username
    else:
        cur=conn.cursor()
        data= (username, password, email)
        cur.execute("""INSERT into login values (?,?,?)""", data)
        conn.commit()
        ask_money(user_id)


def validate(username,password):
    if username == "admin":
        if password == "admin":
            new_app = Tk()
            new_app.title("Portfolio")
            new_app.geometry("800x800")
            new_app.pack_propagate(False)
            new_app.resizable(0, 0)
            cur = conn.cursor()
            cur.execute("""SELECT * FROM portfolio""")
            i =cur.fetchall()
            df = pd.DataFrame(i,columns = ["user_id","symbol","qty","price","Total_value","Total profit"])
            frame1 = tk.LabelFrame(new_app, text="porfiolios")
            frame1.place(height=500, width=800)
            tv1 = ttk.Treeview(frame1)
            tv1.place(relheight=1, relwidth=1)
            treescrolly = tk.Scrollbar(frame1, orient="vertical", command=tv1.yview)
            treescrollx = tk.Scrollbar(frame1, orient="horizontal", command=tv1.xview)
            tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
            treescrollx.pack(side="bottom", fill="x")
            treescrolly.pack(side="right", fill="y")
            tv1["column"] = list(df.columns)
            tv1["show"] = "headings"
            for column in tv1["columns"]:
                tv1.heading(column, text=column)
            df_rows = df.to_numpy().tolist() # turns the dataframe into a list of lists
            for row in df_rows:
                tv1.insert("", "end", values=row)
            newap = Tk()
            newap.title("login")
            newap.geometry("800x800")
            newap.pack_propagate(False)
            newap.resizable(0, 0)
            cur = conn.cursor()
            cur.execute("""SELECT * FROM login""")
            i =cur.fetchall()
            df_1 = pd.DataFrame(i,columns = ["user_id","password","email"])
            frame1 = tk.LabelFrame(newap, text="login")
            frame1.place(height=500, width=800)
            tv1 = ttk.Treeview(frame1)
            tv1.place(relheight=1, relwidth=1)
            treescrolly = tk.Scrollbar(frame1, orient="vertical", command=tv1.yview)
            treescrollx = tk.Scrollbar(frame1, orient="horizontal", command=tv1.xview)
            tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
            treescrollx.pack(side="bottom", fill="x")
            treescrolly.pack(side="right", fill="y")
            tv1["column"] = list(df_1.columns)
            tv1["show"] = "headings"
            for column in tv1["columns"]:
                tv1.heading(column, text=column)
            df_rows = df_1.to_numpy().tolist() # turns the dataframe into a list of lists
            for row in df_rows:
                tv1.insert("", "end", values=row)
        else:
            ID.delete(0,'end')
            PW.delete(0,'end')
            username = ID.get()
            password = PW.get()
            user_id = username
    c = username
    p = password
    print(c,p)
    try:
        if (username_password(conn,c,p)):
         messagebox.showinfo("Successful", "Login Was Successful")
         return True
        else:
         messagebox.showerror("Error", "Wrong Credentials")
         return False
    except IndexError:
         messagebox.showerror("Error", "Wrong Credentials")
         return False

def ask_money(user_id):
    money = askstring('money', 'What is your starting balance?')
    showinfo('Hello!', 'your balance is: {}'.format(money))
    UserMoney(conn, user_id, money)
    main_page(user_id)
def main_page(user_id):
    main_window(user_id)



def window():
    root.title("Bullstocks")
    root.geometry("1023x700")
    root.config(bg="#FA5F1A")
    cur = conn.cursor()
    label_2= Label(root, text="ID",font='lato')
    label_2.place(x= 310,y =20)
    label_2= Label(root, text="password",font='lato')
    label_2.place(x= 310,y =40)
    login = Button(root, text="login",command = Login)
    login.place(x= 580,y =40)
    label_3= Label(root, text="email",font='lato')
    label_3.place(x= 310,y =80)
    register = Button(root, text="Signup",command=Signup)
    register.place(x= 580,y =80)

# submit = Button(root, text="Submit",pady=5, padx=20)
# submit.pack()


#root.mainloop()
def run():
    mainloop()

window()
run()
