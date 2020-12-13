try:
    import Tkinter as tk
except:
    import tkinter as tk
import pandas as pd
import numpy as np
# from ent import root
from tkinter import filedialog, messagebox, ttk
from tkinter import messagebox
import time
from file import *
from buy import *
from tkinter.simpledialog import askstring
from tkinter import filedialog, messagebox, ttk
from tkinter.messagebox import showinfo
from get_all_tickers import get_tickers as gt
import requests
from bs4 import  BeautifulSoup
import bs4
import matplotlib.pyplot as plt
# from login import loginWindow
import sqlite3
conn = sqlite3.connect('Database.db')


def main_window(u):
    global user_id
    user_id =u
    mainapp = Tk()
    mainapp.title("Bullstocks")
    mainapp.geometry("800x500")
    mainapp.config(bg="#FA5F1A")
    b1 = Button(mainapp, text = "buy",command=buy_menu)
    b1.place(x = 600,y = 10)
    b1.config(command=buy_menu)
    sell_b = Button(mainapp, text = "sell",command =sell_menu)
    sell_b.place(x = 700,y = 10)
    trade_history = Button(mainapp, text = "Trade history",command = trd)
    trade_history.place(x = 480,y = 10)
    portfolio = Button(mainapp, text = "Portfolio",command = portfolio_app)
    portfolio.place(x = 380,y = 10)
    sector_index = Button(mainapp, text = "sector index",command=sector_indexes)
    sector_index.place(x = 280,y = 10)
    sock_history = Button(mainapp, text = "stock_history",command = stock_his)
    sock_history.place(x = 150,y = 10)
    sock_performance = Button(mainapp, text = " Portfolio Perfomance",command = p_plot)
    sock_performance.place(x = 10,y = 50)
    indexes = Label(mainapp, text = "Market Indexes")
    indexes.place(x = 400,y = 100)
    indexes.config(font=("Courier", 20))
    sp = Button(mainapp, text = "S&P500",command = table_1)
    sp.place(x = 300,y = 200)
    nsdq = Button(mainapp, text = "NASDAQ",command = table_2)
    nsdq.place(x = 300,y = 250)
    rsl = Button(mainapp, text = "Russel2000",command = table_3)
    rsl.place(x = 300,y = 300)
    MarketIndex("^RUT")
    MarketIndex("^IXIC")
    MarketIndex("^GSPC")
    sp_v = Label(mainapp, text = idx("^GSPC"))
    sp_v.place(x = 400,y = 200)
    nsdq_v = Label(mainapp, text = idx("^IXIC"))
    nsdq_v.place(x = 400,y = 250)
    rsl_v = Label(mainapp, text = idx("^RUT"))
    rsl_v.place(x = 400,y = 300)

    rsl_p = Label(mainapp, text = change("^RUT"))
    rsl_p.place(x = 600,y = 300)
    sp_p = Label(mainapp, text = change("^GSPC"))
    sp_p.place(x = 600,y = 200)
    nsdq_p = Label(mainapp, text = change("^IXIC"))
    nsdq_p.place(x = 600,y = 250)
def table_1():
    new_app = Tk()
    new_app.title("S&P500")
    new_app.geometry("800x800")
    new_app.pack_propagate(False)
    new_app.resizable(0, 0)
    cur = conn.execute("SELECT * from snp500")
    a = cur.fetchall()
    df = pd.DataFrame(a,columns = ["date","open","high","low","adj_close","volume"])
    # df.drop(["volume"],inplace =True,axis = 1)
    frame1 = tk.LabelFrame(new_app, text="snp500")
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
def table_2():
        new_app = Tk()
        new_app.title("NASDAQ")
        new_app.geometry("800x800")
        new_app.pack_propagate(False)
        new_app.resizable(0, 0)
        cur = conn.execute("SELECT * from nasdaq")
        a = cur.fetchall()
        df = pd.DataFrame(a,columns = ["date","open","high","low","adj_close","volume"])
        # df.drop(["volume"],inplace =True,axis = 1)
        frame1 = tk.LabelFrame(new_app, text="nasdaq")
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

def table_3():
        new_app = Tk()
        new_app.title("russell2000")
        new_app.geometry("800x800")
        new_app.pack_propagate(False)
        new_app.resizable(0, 0)
        cur = conn.execute("SELECT * from russell2000")
        a = cur.fetchall()
        df = pd.DataFrame(a,columns = ["date","open","high","low","adj_close","volume"])
        # df.drop(["volume"],inplace =True,axis = 1)
        frame1 = tk.LabelFrame(new_app, text="russell2000")
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
def change(indx):
    curr= conn.cursor()
    curr.execute("""SELECT percent_change FROM dashboard where Indx =?""",(indx,))
    p = curr.fetchall()
    df = pd.DataFrame(p,columns=["percent_change"])
    a= str(df["percent_change"][0]) +"%"
    return a

def idx(indx):
    curr= conn.cursor()
    curr.execute("""SELECT value FROM dashboard where Indx =?""",(indx,))
    p = curr.fetchall()
    df = pd.DataFrame(p,columns=["indx"])
    a= str(df["indx"][0])
    return a
def  price(symbol):
    r = requests.get('https://finance.yahoo.com/quote/' + symbol + '?p=' + symbol)
    soup = bs4.BeautifulSoup(r.text,"lxml")
    price = soup.find("div",{'class': "My(6px) Pos(r) smartphone_Mt(6px)"})
    a = price.find("span").text
    return a

def trd():
    messagebox.showinfo("trade history","A csv file has been created with your trade history")
    Print(user_id)

def MarketIndex(indx):
    val = price(indx)
    val =str(val)
    val =val.replace(",","")
    r = requests.get('https://finance.yahoo.com/quote/' + indx + '?p=' + indx)
    soup = bs4.BeautifulSoup(r.text,"lxml")
    try:
        price_c = soup.find("span",{'class': "Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)"})
        p = price_c.text
    except:
        price_c= soup.find("span",{'class': "Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)"})
        p = price_c.text
    change, p_c = p.split(" ")
    percent_change = p_c.strip('(%)')
    change = float(change)
    percent_change = float(percent_change)
    curr =conn.cursor()
    curr.execute("""select Indx from dashboard""")
    flag = curr.fetchall()
    df=pd.DataFrame(flag,columns = ["Indexes"])
    # val =float(val)
    f= False
    for i in df["Indexes"]:
        print(i,indx)
        if i ==indx:
            f= True
    if f ==False:
        print("ig")
        curr.execute("""INSERT INTO dashboard values(?,?,?,?)""",(indx,val,change,percent_change))
        conn.commit()
    if f ==True:
        curr.execute("""UPDATE dashboard set value =?,change = ?,percent_change =?  WHERE indx = ?""",(val,change,percent_change,indx))
        conn.commit()

def portfolio_app():
    new_app = Tk()
    new_app.title("Portfolio")
    new_app.geometry("800x800")
    new_app.pack_propagate(False)
    new_app.resizable(0, 0)
    TotalValue(user_id)
    UserReturn(user_id)
    cur  = conn.cursor()
    cur.execute(""" Select return from user_return where user_id = ?""",(user_id,))
    a= cur.fetchall()
    a=str(a)
    a = a.strip("([,])")
    r= "Return: " + a +"%"
    frame1 = tk.LabelFrame(new_app, text=r)
    frame1.place(height=500, width=800)
    # ret = Label(frame1, text =a)
    # ret.place(x = 100,y = 200)
    df = fetch_portfolio(user_id)
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
    symbol = askstring('Symbol', 'Enter Symbol')
    qty = askstring('qty', 'Enter Quantity')
    try:
        qty =int(qty)
    except:
        qty = askstring('qty', 'Error! Enter correct Quantity')
    value = price(symbol)
    u=user_id
    buy_stock(u,qty,symbol,value)
    # buy_stock(user_id,qty,s,value)
def stock_his():
    symbol = askstring('Symbol', 'Enter Symbol')
    list_of_tickers = gt.get_tickers()
    flag = False
    for i in list_of_tickers:
        if(i ==symbol):
            flag = True
        if flag == True:
            StockHistory(symbol)

def sell_menu():
    # value = price()
    symbol = askstring('Symbol', 'Enter Symbol')
    qty = askstring('qty', 'Enter Quantity')
    value = price(symbol)
    try:
        qty =int(qty)
    except:
        qty = askstring('qty', 'Enter correct Quantity')
    print(qty)
    trade(conn,user_id,symbol,qty,"sell",value)

def sector_indexes():
    sector_app = Tk()
    sector_app.geometry("800x800")
    sector_app.config(bg="#FA5F1A")
    sector_app.title("Sector Indexes")
    t,tp,b,bp,o,op,e,ep,a,ap = sec_indx()

    s_l = ["Tech","Banks and Finance","Energy","Oil and Gas","Auomobile"]
    indexes = Label(sector_app, text = "Sector Indexes",)
    indexes.place(x = 400,y = 100)
    indexes.config(font=("Courier", 20))
    ti= Label(sector_app, text = s_l[0])
    ti.place(x = 200,y = 200)
    tc = Label(sector_app, text = round(t,2))
    tc.place(x = 350,y = 200)
    tpl = Label(sector_app, text = round(tp,2))
    tpl.place(x = 400,y = 200)

    bi = Label(sector_app, text = s_l[1])
    bi.place(x = 200,y = 250)
    bc= Label(sector_app, text = round(b,2))
    bc.place(x = 350,y = 250)
    bpl = Label(sector_app, text = round(bp,2))
    bpl.place(x = 400,y = 250)

    ei = Label(sector_app, text = s_l[2])
    ei.place(x = 200,y = 300)
    ec= Label(sector_app, text = round(e,2))
    ec.place(x = 350,y = 300)
    epl = Label(sector_app, text = round(ep,2))
    epl.place(x = 400,y = 300)

    oi = Label(sector_app, text = s_l[3])
    oi.place(x = 200,y = 350)
    oc= Label(sector_app, text = round(o,2))
    oc.place(x = 350,y = 350)
    opl = Label(sector_app, text = round(op,2))
    opl.place(x = 400,y = 350)

    ai = Label(sector_app, text = s_l[4])
    ai.place(x = 200,y = 400)
    ac= Label(sector_app, text = round(a,2))
    ac.place(x = 350,y = 400)
    apl = Label(sector_app, text = round(ap,2))
    apl.place(x = 400,y = 400)

    new_app = Tk()
    new_app.title("sector_indexes")
    new_app.geometry("800x800")
    new_app.pack_propagate(False)
    new_app.resizable(0, 0)
    d = {"Tech" :['AMZN','GOOG','FB','AAPL','MSFT'],
        "BanksAndFinance" :["JPM","BAC","C","GS","HSBC"],
        "OilAndGas" : ['CVX','XOM','RDS-A','TOT','BP'],
        "Energy" : ['PTR','COP','SLB','EPD','E'],
        "Automobile" : ['TSLA','F','TYO','VWAGY','RACE']}
    df = pd.DataFrame(data=d)
    frame1 = tk.LabelFrame(new_app, text="Sectors")
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
def p_plot():
    cur = conn.cursor()
    cur.execute("""SELECT return FROM
    user_return WHERE user_id = ?""",(user_id,))
    ret = cur.fetchall()
    ret =str(ret)
    ret = ret.strip("([,])")
    if ret!= "":
        ret = float(ret)
    else:
        messagebox.showerror("error", "portfolio empty")
        return
    cur.execute("""SELECT change FROM
    dashboard WHERE Indx = ?""",("^GSPC",))
    val = cur.fetchall()
    val =str(val)
    val = val.strip("([,])")
    val = float(val)
    data = {"S&P500":val,"Porfolio":ret}
    x= list(data.keys())
    y= list(data.values())
    plt.figsize = (5,4)
    plt.title("Performance of the porfolio relative to the S&P 500")
    plt.ylabel("percentage change")
    plt.bar(x,y,width = 0.2)
    plt.show()

def buy_stock(user_id,qty,symbol,price):
    curr= conn.cursor()
    user= (user_id)
    list_of_tickers = gt.get_tickers()
    flag = True
    for i in list_of_tickers:
        if(i ==symbol):
            flag = True
    if flag == True:
        curr.execute("""Select cash from user_money where user_id = ?;""",(user_id,))
        um=curr.fetchall()
        um =str(um)
        price =str(price)
        pr = price.replace(',' ,'')
        p=float(pr)
        qty=float(qty)
        commsion = float(0.01 *(qty*p))
        total =qty*p
        print(um)
        print(user_id)
        um=float(um.strip("([,])"))
        if(total +commsion > um):
            print("error")
            messagebox.showerror("Error", "your dont have enough balance")
        else:
            print("trading")
            curr.execute("""Select cash from user_money where user_id = ?;""",(user_id,))
            trade(conn,user_id,symbol,qty,"buy",p)
    else:
        messagebox.showerror("Error", "Symbol Not found")

def StockHistory(Stk_smbl):
    import pandas as pd
    from pandas_datareader import data
    import matplotlib.pyplot as plt
    import numpy as np
    #import time
    from datetime import datetime
    import datetime
    start_date = datetime.datetime.now().date() - datetime.timedelta(days=5*365)
    end_date = datetime.datetime.now().date()


    symbol = Stk_smbl
    stock_data = data.DataReader(Stk_smbl, 'yahoo', start_date, end_date)


    close = stock_data['Close']


    all_weekdays = pd.date_range(start = start_date, end= end_date, freq='B')


    close = close.reindex(all_weekdays)

    close = close.fillna(method='ffill')

    stock = close
    # Calculate the 20 and 100 days moving averages of the closing prices
    short_rolling_stock = stock.rolling(window=20).mean()
    long_rolling_stock = stock.rolling(window=100).mean()

    # Plot everything by leveraging the very powerful matplotlib package
    plt.rcParams.update({'font.size': 24})
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(16,19))

    ax.plot(stock.index, stock, label= Stk_smbl, color ='#FFE01B', linewidth = '0.5')
    #ax.plot(short_rolling_stock.index, short_rolling_stock, label='20 days rolling', color ='red',linewidth = '2')
    #ax.plot(long_rolling_stock.index, long_rolling_stock, label='100 days rolling')

    ax.set_xlabel('Date')
    ax.set_ylabel('Adjusted closing price ($)')
    ax.set_title('STOCK HISTORY')
    ax.legend()
    plt.grid(True)
    plt.fill_between(stock.index,stock, color = '#FFE01B')
    plt.tight_layout()
    plt.show()
#
#
# main_window(user_id)
# mainloop()
