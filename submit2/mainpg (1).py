from tkinter import *
from tkinter import messagebox
import time
from buy import *
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
from tkinter.ttk import *

# from login import loginWindow
import sqlite3
conn = sqlite3.connect('Database.db')

# mainapp = Tk()
# def main_window():
# mainapp.title("Bullstocks")
# mainapp.geometry("800x500")
# mainapp.config(bg="#FA5F1A")
# b1 = Button(mainapp, text = "buy",command= buy())
# b1.place(x = 600,y = 10)
# sell_b = Button(mainapp, text = "sell",command = sell())
# sell_b.place(x = 700,y = 10)
# sell_b = Button(mainapp, text="Sell",pady=5,relief=FLAT, padx=20,bg='#4D5F75',fg='white')
# sell_b.place(200,400)

def buy(user_id,qty,symbol,price):
    curr= conn.cursor()
    user= (user_id)
    curr.execute("""Select cash from user_money where user_id = ?;""",(user_id,))
    um=curr.fetchall()
    um =str(um)
    commsion = 0.01 *(qty*price)
    total =qty*price
    um=int(um.strip("([,])")))
    if(total +commsion > um):
        messagebox.showerror("Error", "your dont have enough balance")
    else:
        curr.execute("""Select cash from user_money where user_id = ?;""",(user_id,))


def sell(symbol, qty, user_id ):

    curr=conn.cursor()
    user=(user_id)
    curr.execute("""Select symbol from portfolio where user_id = ? and symbol =?;""",[(user_id,),(symbol)])
    abc=curr.fetchall()
    curr.execute("""UPDATE portfolio SET qty=(abc+1) WHERE qty=abc""")
    #update qty
    #if qty=0, remove symb
    conn.commit()

buy("hj")
# mainloop()
