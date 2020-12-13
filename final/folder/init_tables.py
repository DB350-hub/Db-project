
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import sqlite3
conn = sqlite3.connect('Database.db')

c =  conn.cursor()

c.execute("""CREATE TABLE login
(
user_id varchar(10) primary key,
password varchar(16) NOT NULL,
email varchar (20),
CONSTRAINT FK_user_id FOREIGN KEY (user_id) REFERENCES user_money(user_id)
)""")

c.execute(""" CREATE TABLE user_money
(
user_id varchar(10),
cash numeric,
starting_cash numeric,
CONSTRAINT FK_user_id FOREIGN KEY (user_id) REFERENCES login(user_id)
)""")

c.execute("""
CREATE TABLE user_return
(user_id varchar(10) Primary key,
return numeric,
total_account_value numeric,
CONSTRAINT FK_user_id FOREIGN KEY (user_id) REFERENCES portfolio(user_id)
)""")

c.execute("""
CREATE TABLE trade_history
( trade_id varchar(10) PRIMARY KEY,
symbol varchar(10),
trade_type Bit,
Qty numeric,
Price NUMERIC,
user_id varchar(10),
CONSTRAINT FK_user_id FOREIGN KEY (user_id) REFERENCES login(user_id)
)""")

c.execute("""
CREATE TABLE portfolio
(
user_id varchar(10),
symbol varchar (10),
qty int,
purchase_price numeric,
total_value numeric,
total_profit numeric,
CONSTRAINT FK_user_id FOREIGN KEY (user_id) REFERENCES portfolio(user_id),
CONSTRAINT FK_symbol FOREIGN KEY (symbol) REFERENCES trade_history(symbol)
)""")

c.execute("""CREATE TABLE snp500
(
date_ date PRIMARY KEY,
open numeric,
high numeric,
low numeric,
adj_close numeric,
volume numeric
)""")


c.execute("""CREATE TABLE nasdaq
(
date_ date PRIMARY KEY,
open numeric,
high numeric,
low numeric,
adj_close numeric,
volume numeric
)""")

c.execute("""CREATE TABLE russell2000
(
date_ date PRIMARY KEY,
open numeric,
high numeric,
low numeric,
adj_close numeric,
volume numeric
)""")

c.execute("""CREATE TABLE dashboard
(
Indx varchar(20) PRIMARY KEY,
value  numeric,
change numeric,
percent_change numeric
)""")

c.execute("""CREATE TABLE sector_index
(
indx varchar(20) PRIMARY KEY,
value numeric,
change numeric,
percent_change numeric
)""")
conn.commit()
cur = conn.cursor()
SnP = pd.read_csv("^GSPC.csv")
NDQ = pd.read_csv("^IXIC.csv")
R = pd.read_csv("^RUT.csv")
NDQ["Volume"] = NDQ["Volume"].astype("float64")
SnP["Volume"] = SnP["Volume"].astype("float64") 
R.dropna(inplace=True)

cur = conn.cursor()
for i in range(5030):
    cur.execute("""INSERT into snp500 values(?,?,?,?,?,?)""",(SnP["Date"][i],SnP["Open"][i],
    SnP["High"][i],SnP["Low"][i],SnP["Adj Close"][i],SnP["Volume"][i]))
    conn.commit()

for i in range(4981):
    cur.execute("""INSERT into russell2000 values(?,?,?,?,?,?)""",(R["Date"][i],R["Open"][i],
    R["High"][i],R["Low"][i],R["Adj Close"][i],R["Volume"][i]))
    conn.commit()

for i in range(5030):
    cur.execute("""INSERT into nasdaq values(?,?,?,?,?,?)""",(NDQ["Date"][i],NDQ["Open"][i],
    NDQ["High"][i],NDQ["Low"][i],NDQ["Adj Close"][i],NDQ["Volume"][i]))
    conn.commit()
