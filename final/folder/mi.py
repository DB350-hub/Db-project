
import pandas_datareader.data as web
from datetime import datetime
import datetime
import numpy as np
import pandas as pd
import sqlite3
import bs4
import requests
from bs4 import BeautifulSoup
from mainpg import price
conn = sqlite3.connect('Database.db')
#
# def  price(symbol):
#     r = requests.get('https://finance.yahoo.com/quote/' + symbol + '?p=' + symbol)
#     soup = bs4.BeautifulSoup(r.text,"lxml")
#     price = soup.find("div",{'class': "My(6px) Pos(r) smartphone_Mt(6px)"})
#     a = price.find("span").text
#     return a

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
# MarketIndex("^RUT")
def change(indx):
    curr= conn.cursor()
    curr.execute("""SELECT percent_change FROM dashboard where Indx =?""",(indx,))
    p = curr.fetchall()
    df = pd.DataFrame(p,columns=["percent_change"])
    return df["percent_change"][0]

def idx(indx):
    curr= conn.cursor()
    curr.execute("""SELECT value FROM dashboard where Indx =?""",(indx,))
    p = curr.fetchall()
    df = pd.DataFrame(p,columns=["indx"])
    a= str(df["indx"][0])
    return a
print(idx("^RUT"))
