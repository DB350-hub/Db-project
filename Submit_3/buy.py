import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
from tkinter.ttk import *
import time
import pandas as pd
import numpy as np
conn = sqlite3.connect('Database.db')

def trade(conn,user_id,symbol,qty,type,price):
  cur = conn.cursor()
  cur.execute("SELECT trade_id FROM trade_history")
  T_id = cur.fetchall()
  #print(len(T_id))
  i = len(T_id)
  if i == 0:
    i = 1
  else:
    i += 1

  if type == "buy":
    print("in_buy")
    cur = conn.cursor()
    data= (i,symbol,type,qty,price,user_id)
    cur.execute(""" INSERT INTO trade_history
    values (?,?,?,?,?,?)""",data)
    cur.execute("""Select symbol from portfolio where symbol =?""",(symbol,))
    um=cur.fetchall()
    cur.execute(""" Select qty from portfolio
    where symbol = ?""",(symbol,))
    b_qty=cur.fetchall()

    cur.execute(""" Select cash from user_money
    where user_id = ?""",(user_id,))
    cash=cur.fetchall()
    cash =str(cash)
    cash = cash.strip("([,])")
    cash = int(cash)

    b_qty =str(b_qty)
    b_qty = b_qty.strip("([,])")
    um =str(um)
    um=um.strip("([,])")
    # print(b_qty,"um")
    if (um ==""):
        new_qty =qty
        total_v = qty*price
        new_cash = cash - total_v
        data_2 = (user_id,symbol,qty,price,None,None)
        cur.execute(""" INSERT INTO portfolio
        values (?,?,?,?,?,?)""",data_2)
        print("new_cash",new_cash)
        cur.execute(""" UPDATE user_money
        SET cash = ? WHERE user_id=?""",(new_cash,user_id))
        conn.commit()
    else:
        b_qty = int(b_qty)
        # print(b_qty,"89")
        new_qty =b_qty + qty
        total_v = qty*price
        new_cash = cash - total_v
        cur.execute(""" UPDATE portfolio
        SET qty = ? WHERE symbol=?""",(new_qty,symbol,))
        print("new_cash2",new_cash)
        cur.execute(""" UPDATE user_money
        SET cash = ? WHERE user_id=?""",(new_cash,user_id))
        conn.commit()
    conn.commit()
    print("stock added")
    # print (i)

  if type == 'sell':
    data= (i,symbol,type,qty,price,user_id)
    curr=conn.cursor()
    user=(user_id)
    curr.execute("""Select symbol from portfolio where user_id = ? and symbol =?;""",(user_id,symbol))
    abc=curr.fetchall()
    b_qty= curr.execute(""" Select qty from portfolio where symbol =?""",(symbol,))
    b_qty=curr.fetchall()
    b_qty =str(b_qty)
    b_qty = b_qty.strip("([,])")
    if(b_qty != ''):
         b_qty = int(b_qty)
    cur.execute(""" Select cash from user_money
    where user_id = ?""",(user_id,))
    cash=cur.fetchall()
    cash =str(cash)
    cash = cash.strip("([,])")
    cash = float(cash)

    if(b_qty==qty):
        new_cash = (price* qty) +cash
        print(cash,"p1")
        curr.execute("""DELETE FROM portfolio Where user_id=? and symbol=?""",(user_id,symbol))
        cur.execute(""" UPDATE user_money
        SET cash = ? WHERE user_id=?""",(new_cash,user_id))
        conn.commit()

    elif (b_qty>qty):
        cash =float(cash)
        price =float(price)
        qty =int(qty)
        new_cash = (price* qty) +cash
        print("in_new qty")
        new = b_qty -qty
        print(new_cash,"p2")
        curr.execute("""UPDATE portfolio SET qty=? where user_id = ? and symbol= ?""",(new,user_id,symbol))
        cur.execute(""" UPDATE user_money
        SET cash = ? WHERE user_id=?""",(new_cash,user_id))
        conn.commit()

    elif (qty >b_qty):
        messagebox.showerror("Trade Failed", "The quantity of the stock is higher than the portofolio")

    curr.execute(""" INSERT INTO trade_history
    values (?,?,?,?,?,?)""",data)
    conn.commit()
    print("stock sold")
    # print (i)

# trade(conn,"bgtb","AMZN",120,"sell",300)
# trade(conn,"abc","AMZN",50,"sell",100)

def m(conn, user_id, cash):
    UID = user_id
    U_cash = cash
    cur = conn.cursor()
    data = (UID, U_cash)
    cur.execute("""INSERT into user_money values(?,?)""", data)
    conn.commit()

def UserMoney(conn, user_id, cash):
    m(conn, user_id, cash)

def fetch_portfolio(user_id):
    cur = conn.cursor()
    cur.execute("""SELECT symbol,qty,purchase_price,total_value,total_profit FROM
    portfolio WHERE user_id = ?""",(user_id,))
    a = cur.fetchall()
    df = pd.DataFrame(a,columns = ["Symbol","Quantity","Price","total_value","Total Profit"])
    return df
