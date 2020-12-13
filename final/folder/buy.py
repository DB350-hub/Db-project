import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
from tkinter.ttk import *
import time
import pandas as pd
import numpy as np
import requests
from bs4 import  BeautifulSoup
import bs4

conn = sqlite3.connect('Database.db')

def  price_x(symbol):
    r = requests.get('https://finance.yahoo.com/quote/' + symbol + '?p=' + symbol)
    soup = bs4.BeautifulSoup(r.text,"lxml")
    price = soup.find("div",{'class': "My(6px) Pos(r) smartphone_Mt(6px)"})
    a = price.find("span").text
    a= str(a)
    flag = False
    if ','in a:
        pr = a.replace(',' ,'')
        return pr
    else:
        return a

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
    cur.execute("""Select symbol from portfolio where symbol =? and user_id = ?""",(symbol,user_id))
    um=cur.fetchall()
    cur.execute(""" Select qty from portfolio
    where symbol = ?""",(symbol,))
    b_qty=cur.fetchall()

    cur.execute(""" Select cash from user_money
    where user_id = ?""",(user_id,))
    cash=cur.fetchall()
    cash =str(cash)
    cash = cash.strip("([,])")
    cash = float(cash)

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
        print(um,"um")
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
    print(abc)
    abc =str(abc)
    abc = abc.strip("[,]")
    if abc == '':
        messagebox.showerror("Trade Failed", "Stock not in portfolio")
        return
    b_qty= curr.execute(""" Select qty from portfolio where symbol =? and user_id =?""",(symbol,user_id))
    b_qty=curr.fetchall()
    b_qty =str(b_qty)
    b_qty = b_qty.strip("([,])")
    if(b_qty != ''):
         b_qty = int(b_qty)
    else:
        b_qty =0
    cur.execute(""" Select cash from user_money
    where user_id = ?""",(user_id,))
    cash=cur.fetchall()
    cash =str(cash)
    cash = cash.strip("([,])")
    cash = float(cash)
    price =str(price)
    pr = price.replace(',' ,'')
    price =float(pr)
    if(b_qty==qty):
        new_cash = (float(price)* int(qty)) + cash
        print(cash,"p1")
        curr.execute("""DELETE FROM portfolio Where user_id=? and symbol=?""",(user_id,symbol))
        cur.execute(""" UPDATE user_money
        SET cash = ? WHERE user_id=?""",(new_cash,user_id))
        conn.commit()

    if (b_qty > qty):
        cash =float(cash)
        qty =int(qty)
        new_cash = (price* qty) +cash
        print("in_new qty")
        new = b_qty -qty
        print(new_cash,"p2")
        curr.execute("""UPDATE portfolio SET qty=? where user_id = ? and symbol= ?""",(new,user_id,symbol))
        cur.execute(""" UPDATE user_money
        SET cash = ? WHERE user_id=?""",(new_cash,user_id))
        conn.commit()

    if (qty > b_qty):
        messagebox.showerror("Trade Failed", "The quantity of the stock is higher than the portofolio")
        return
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
    data = (UID, U_cash,U_cash)
    cur.execute("""INSERT into user_money values(?,?,?)""", data)
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
def TotalValue(user_id):
    cur = conn.cursor()
    cur.execute("""SELECT starting_cash FROM
    user_money WHERE user_id = ?""",(user_id,))
    cash = cur.fetchall()
    cash =str(cash)
    cash = cash.strip("([,])")
    cash = float(cash)

    cur.execute("""SELECT symbol,qty,purchase_price FROM
    portfolio WHERE user_id = ?""",(user_id,))

    a =cur.fetchall()
    df = pd.DataFrame(a,columns= ["symbol","qty","purchase price"])
    df["curr price"] = [float(price_x(x)) for x in df.symbol]
    x =list()
    for i in range(len(df["curr price"])):
        x.append((df["curr price"][i]*df["qty"][i]))
    f= False
    df ["total value"] = x
    y =list()
    for i in range(len(x)):
        s = (df ["total value"][i]) - (df["qty"][i] * df["purchase price"][i])
        y.append(s)
    df ["Total gain/loss"] = y
        # for i in range(len(x)):
        #     cur.execute("""INSERT INTO portfolio(total_value,total_profit) VALUES(?,?) where user_id =? and symbol =?""",(x[i],y[i],user_id,df["symbol"][i],))
        #     conn.commit()
    for i in range(len(x)):
        cur.execute("""UPDATE portfolio set total_value =?,total_profit =?  WHERE user_id = ? and symbol =?""",(x[i],y[i],user_id,df["symbol"][i],))
        conn.commit()

def UserReturn(user_id): #///CHANGE MADE///

    cur = conn.cursor()
    cur.execute("""SELECT starting_cash FROM
    user_money WHERE user_id = ?""",(user_id,))
    cash = cur.fetchall()
    cash =str(cash)
    cash = cash.strip("([,])")
    cash = float(cash)
    cur.execute("""SELECT cash FROM
    user_money WHERE user_id = ?""",(user_id,))
    new_cash = cur.fetchall()
    new_cash =str(new_cash)
    new_cash = new_cash.strip("([,])")
    new_cash = float(new_cash)
    cur.execute("""SELECT SUM(total_value) FROM
    portfolio WHERE user_id = ? """,(user_id,))
    total = cur.fetchall()
    total =str(total)
    total = total.strip("([,])")
    if total == 'None':
        cur.execute("""INSERT INTO user_return values(?,?,?)""",(user_id,0,0))
        conn.commit()
        return
    total = float(total)
    Total_value = total +new_cash
    User_return = (Total_value - cash)/cash
    User_return *= 100
    f= False
    cur.execute("""select return from user_return where user_id = ?""",(user_id,))
    flag = str(cur.fetchall())
    flag = flag.strip("[(,)]")
    flag = [flag]
    for i in flag:
        if i =="":
            f= True
            print("true")
    # print(flag)
    if f ==True:
        print("ig")
        cur.execute("""INSERT INTO user_return values(?,?,?)""",(user_id,User_return,Total_value))
        conn.commit()
    else:
        print("i")
        cur.execute("""UPDATE user_return set return =?,total_account_value = ? WHERE user_id = ?""",(User_return,Total_value,user_id))
        conn.commit()
