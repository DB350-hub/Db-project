try:
    import Tkinter as tk
except:
    import tkinter as tk
import pandas as pd
import numpy as np
# from ent import *
from tkinter.ttk import *
from tkinter import messagebox
import time
from buy import *
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
from get_all_tickers import get_tickers as gt

# from login import loginWindow
import sqlite3
conn = sqlite3.connect('Database.db')
user_id = "abc"
mainapp = Tk()
def main_window(user_id):
    mainapp.title("Bullstocks")
    mainapp.geometry("800x500")
    # mainapp.config(bg="#FA5F1A")
    b1 = Button(mainapp, text = "buy",command=buy_menu)
    b1.place(x = 600,y = 10)
    sell_b = Button(mainapp, text = "sell",command =sell_menu)
    sell_b.place(x = 700,y = 10)
    trade_history = Button(mainapp, text = "Trade history",command = trd)
    trade_history.place(x = 480,y = 10)

def  price():
    return 100

def trd():
    messagebox.showinfo("trade history","A csv file has been created with your trade history")
    Print(user_id)

def Print(user_id):
  curr = conn.cursor()
  i = 0
  curr.execute("""SELECT * FROM trade_history WHERE user_id = ?;""", (user_id,))
  th =curr.fetchall()
  df = pd.DataFrame(th,columns = ["Trade ID","Symbol","Trade Type","Quantity","Price","user_id"])
  df_final = df[["Symbol","Trade Type","Quantity","Price"]]
  var = "Trade history"+ user_id
  df_final.to_csv(var)

def buy_menu():
    value = price()
    symbol = askstring('Symbol', 'Enter Symbol')
    qty = askstring('qty', 'Enter Quantity')
    buy_stock(user_id,qty,symbol,value)
    # buy_stock(user_id,qty,s,value)
def sell_menu():
    value = price()
    symbol = askstring('Symbol', 'Enter Symbol')
    qty = askstring('qty', 'Enter Quantity')
    qty =int(qty)
    trade(conn,user_id,symbol,qty,"sell",value)
# def TradeHistory(user_id):
  # app = Tk()
  # app.geometry("400x250")
#   label = Label(app, text="TRADE HISTORY")
#   label.pack()
#   TH = Button(app, text="Display History", pady=5, padx=30 )
#   TH.place(x=130, y=80)
#   Print(user_id)

def buy_stock(user_id,qty,symbol,price):
    curr= conn.cursor()
    user= (user_id)
    list_of_tickers = gt.get_tickers()
    for i in list_of_tickers:
        if(i ==symbol):
            flag = True
    if flag == True:
        curr.execute("""Select cash from user_money where user_id = ?;""",(user_id,))
        um=curr.fetchall()
        um =str(um)
        price=float(price)
        qty=float(qty)
        commsion = int(0.01 *(qty*price))
        total =qty*price
        um=int(um.strip("([,])"))
        if(total +commsion > um):
            print("error")
            messagebox.showerror("Error", "your dont have enough balance")
        else:
            print("trading")
            curr.execute("""Select cash from user_money where user_id = ?;""",(user_id,))
            trade(conn,user_id,symbol,qty,"buy",price)
    else:
        messagebox.showerror("Error", "Symbol Not found")
#
#
main_window(user_id)
mainapp.mainloop()
