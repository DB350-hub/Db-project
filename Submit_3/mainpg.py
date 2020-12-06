try:
    import Tkinter as tk
except:
    import tkinter as tk
import pandas as pd
import numpy as np
# from ent import *
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

# from login import loginWindow
import sqlite3
conn = sqlite3.connect('Database.db')
user_id = "erh"

def main_window(user_id):
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
    indexes = Label(mainapp, text = "Market Indexes",)
    indexes.place(x = 400,y = 100)
    indexes.config(font=("Courier", 20))
    sp = Label(mainapp, text = "S&P500")
    sp.place(x = 300,y = 200)
    sp_v = Label(mainapp, text = price("^GSPC"))
    sp_v.place(x = 400,y = 200)
    nsdq = Label(mainapp, text = "NASDAQ")
    nsdq.place(x = 300,y = 250)
    nsdq_v = Label(mainapp, text = price("^IXIC"))
    nsdq_v.place(x = 400,y = 250)
    rsl = Label(mainapp, text = "Russel2000")
    rsl.place(x = 300,y = 300)
    rsl_v = Label(mainapp, text = price("^RUT"))
    rsl_v.place(x = 400,y = 300)



def  price(symbol):
    r = requests.get('https://finance.yahoo.com/quote/' + symbol + '?p=' + symbol)
    soup = bs4.BeautifulSoup(r.text,"lxml")
    price = soup.find("div",{'class': "My(6px) Pos(r) smartphone_Mt(6px)"})
    a = price.find("span").text
    return a

def trd():
    messagebox.showinfo("trade history","A csv file has been created with your trade history")
    Print(user_id)

def portfolio_app():
    new_app = Tk()
    new_app.title("Portfolio")
    new_app.geometry("500x500")
    new_app.pack_propagate(False)
    new_app.resizable(0, 0)
    frame1 = tk.LabelFrame(new_app, text="Return:")
    frame1.place(height=500, width=500)
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
    value = price(symbol)
    qty = askstring('qty', 'Enter Quantity')
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
    value = price(symbol)
    qty = askstring('qty', 'Enter Quantity')
    qty =int(qty)
    trade(conn,user_id,symbol,qty,"sell",value)

def sector_indexes():
    sector_app = Tk()
    sector_app.geometry("800x800")
    sector_app.config(bg="#FA5F1A")
    sector_app.title("Sector Indexes")


    s_l = ["Tech","Banks and Finance","Energy","Oil and Gas","Transportation"]
    indexes = Label(sector_app, text = "sector Indexes",)
    indexes.place(x = 400,y = 100)
    indexes.config(font=("Courier", 20))
    sp = Label(sector_app, text = s_l[0])
    sp.place(x = 300,y = 200)
    nsdq = Label(sector_app, text = s_l[1])
    nsdq.place(x = 300,y = 250)
    rsl = Label(sector_app, text = s_l[2])
    rsl.place(x = 300,y = 300)
    rsl1 = Label(sector_app, text = s_l[2])
    rsl1.place(x = 300,y = 350)
    rsl2 = Label(sector_app, text = s_l[3])
    rsl2.place(x = 300,y = 400)
    rsl3 = Label(sector_app, text = s_l[4])
    rsl3.place(x = 300,y = 450)
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
    flag = True
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
        print(um)
        print(user_id)
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

    # Using pandas_reader.data.DataReader to load the desired data
    symbol = Stk_smbl
    stock_data = data.DataReader(Stk_smbl, 'yahoo', start_date, end_date)

    # Getting just the adjusted closing prices. This will return a Pandas DataFrame
    # The index in this DataFrame is the major index of the panel_data.
    close = stock_data['Close']

    # Getting all weekdays between start date and end date
    all_weekdays = pd.date_range(start = start_date, end= end_date, freq='B')

    # How do we align the existing prices in adj_close with our new set of dates?
    # All we need to do is reindex close using all_weekdays as the new index
    close = close.reindex(all_weekdays)

    # Reindexing will insert missing values (NaN) for the dates that were not present
    # in the original set. To cope with this, we can fill the missing by replacing them
    # with the latest available price for each instrument.
    close = close.fillna(method='ffill')

    stock = close
    # Calculate the 20 and 100 days moving averages of the closing prices
    short_rolling_stock = stock.rolling(window=20).mean()
    long_rolling_stock = stock.rolling(window=100).mean()

    # Plot everything by leveraging the very powerful matplotlib package
    plt.rcParams.update({'font.size': 24})
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(30,20))

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
main_window(user_id)
mainloop()
