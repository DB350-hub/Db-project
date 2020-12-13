


CREATE TABLE login
(user_id varchar(10) primary key,
password varchar(16) NOT NULL,
email varchar (20) NOT NULL,
CONSTRAINT FK_user_id FOREIGN KEY (user_id) REFERENCES user_money(user_id)
);

CREATE TABLE user_money
(
user_id varchar(10),
cash numeric,
starting_cash numeric,
CONSTRAINT FK_user_id FOREIGN KEY (user_id) REFERENCES login(user_id)
);

CREATE TABLE user_return
(user_id varchar(10) Primary key,
return numeric,
total_account_value numeric,
CONSTRAINT FK_user_id FOREIGN KEY (user_id) REFERENCES portfolio(user_id)
);

CREATE TABLE trade_history
( trade_id varchar(10) PRIMARY KEY,
symbol varchar(10),
trade_type Bit,
Qty numeric,
Price NUMERIC,
user_id varchar(10),
CONSTRAINT FK_user_id FOREIGN KEY (user_id) REFERENCES login(user_id)
);

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
);

CREATE TABLE snp500
(
date_ date PRIMARY KEY,
open numeric,
high numeric,
low numeric,
adj_close numeric,
volume numeric
);

CREATE TABLE nasdaq
(
date_ date PRIMARY KEY,
open numeric,
high numeric,
low numeric,
adj_close numeric,
volume numeric
);


CREATE TABLE  russell2000
(
date_ date PRIMARY KEY,
open numeric,
high numeric,
low numeric,
adj_close numeric,
volume numeric
);

CREATE TABLE dashboard
(
Indx varchar(20) PRIMARY KEY,
value  numeric,
change numeric,
percent_change numeric
);

CREATE TABLE sector_index
(
indx varchar(20) PRIMARY KEY,
value numeric,
change numeric,
percent_change numeric
);
