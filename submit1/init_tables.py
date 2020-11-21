import sqlite3
conn = sqlite3.connect('Database.db')

c =  conn.cursor()

c.execute("""CREATE TABLE login
(user_id varchar(10) primary key,
password varchar(16) NOT NULL,
email varchar (20) NOT NULL,
CONSTRAINT FK_user_id FOREIGN KEY (user_id) REFERENCES user_money(user_id)
)
""")
c.execute(""" CREATE TABLE user_money
(
user_id varchar(10),
cash numeric,
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
perchase_price numeric,
total_value numeric,
total_profit numeric,
 CONSTRAINT FK_user_id FOREIGN KEY (user_id) REFERENCES portfolio(user_id),
  CONSTRAINT FK_symbol FOREIGN KEY (symbol) REFERENCES trade_history(symbol)
)
""")
c.execute("""
CREATE TABLE banks_finance
(
symbol varchar (10),
company_name varchar(20),
last_price numeric,
change numeric,
percent_change numeric
)
""")
c.execute("""CREATE TABLE snp500
(

date_ date,
open numeric,
high numeric,
low numeric,
adj_close numeric,
volume numeric
)""")
c.execute("""
CREATE TABLE tech
(
symbol varchar (10),
company_name varchar(20),
last_price numeric,
change numeric,
percent_chage numeric)
""")
c.execute("""
CREATE TABLE energy
(
symbol varchar(10),
company_name varchar(20),
last_price numeric,
change numeric,
percent_change numeric

)""")
c.execute("""CREATE TABLE nasdaq
(
date_ date,
open numeric,
high numeric,
low numeric,
adj_close numeric,
volume numeric
)""")
c.execute("""
CREATE TABLE automobile
(
symbol varchar(10),
company_name varchar(20),
last_price numeric,
change numeric,
percent_change numeric
)""")

c.execute("""CREATE TABLE oilngas

(
symbol varchar (10),
company_name varchar(20),
last_price numeric,
change numeric,
percent_change numeric

)""")

c.execute("""CREATE TABLE dashboard
(
Indx int,
value  numeric,
change numeric,
percent_change numeric
)""")
c.execute("""CREATE TABLE sector_index
(
indx int,
value numeric,
change numeric,
percent_change numeric
)""")
