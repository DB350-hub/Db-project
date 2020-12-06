#!/usr/bin/env python
# coding: utf-8

# In[21]:
def sec_indx():


    from yahoofinancials import YahooFinancials
    import bs4
    import requests
    from bs4 import BeautifulSoup
    import sqlite3
    conn = sqlite3.connect('Database.db')

    # In[30]:


    BanksAndFinance = ["JPM","BAC","C","GS","HSBC"]
    Automobile = ['TSLA','F','TYO','VWAGY','RACE']
    Tech = ['AMZN','GOOG','FB','AAPL','MSFT']
    OilAndGas = ['CVX','XOM','RDS-A','TOT','BP']
    Energy = ['PTR','COP','SLB','EPD','E']

    def SectorIndex(sector):
    #     sector_list = [BanksAndFinance, Automobile, Tech, OilAndGas, Energy]
    #     for sector in sector_list:
        sum_c = []
        sum_pchange = []
        for ticker in sector:
            r = requests.get('https://finance.yahoo.com/quote/' + ticker + '?p=' + ticker)
            soup = bs4.BeautifulSoup(r.text,"lxml")
            try:
                price = soup.find("span",{'class': "Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)"})
                p = price.text
            except:
                price = soup.find("span",{'class': "Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)"})
                p = price.text
            change, p_c = p.split(" ")
            percent_change = p_c.strip('(%)')
            sum_c.append(float(change))
            sum_pchange.append(float(percent_change))
        sumi = sum(sum_c)
        sum_change = sum(sum_c)/5
        sum_percentchange = sum(sum_pchange)/5
        return sumi,sum_change, sum_percentchange

    st,t,tp = SectorIndex(Tech)
    sb,b,bp = SectorIndex(BanksAndFinance)
    so,o,op = SectorIndex(OilAndGas)
    se,e,ep = SectorIndex(Energy)
    sa,a,ap = SectorIndex(Automobile)
    # st,t,tp =1,2,3
    # sb,b,bp = 1,2,3
    # so,o,op = 1,2,3
    # se,e,ep = 1,2,3
    # sa,a,ap = 1,2,3
    def db(conn,st,t,tp,sec):
        cur = conn.cursor()
        f= False
        cur.execute("""select indx from sector_index""")
        flag = str(cur.fetchall())
        flag = flag.strip("[]")
        for i in flag:
            if i ==sec:
                f= True
        print(flag)
        if f ==False:
            print("ig")
            cur.execute("""INSERT INTO sector_index values(?,?,?,?)""",(sec,st,t,tp))
            conn.commit()
        else:
            print("i")
            cur.execute("""UPDATE sector_index set value =?,change = ?,percent_change =?  WHERE indx = ?""",(st,t,tp,sec))
            conn.commit()
    # In[22]:
    db(conn,st,t,tp,"tech")
    db(conn,sb,b,bp,"BanksAndFinance")
    db(conn,so,o,op,"OilAndGas")
    db(conn,se,e,ep,"Energy")
    db(conn,sa,a,ap,"Automobile")
    return t,tp,b,bp,o,op,e,ep,a,ap

# In[ ]:
