import sqlite3

#########
##db
#########



def create_Tables():
    # initialisation db/db, create db
    conn = sqlite3.connect('./db/okcoin_btc_usd.db', check_same_thread=False)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS data (name STR, timestamp INT, price FLOAT, v_bid FLOAT, v_ask FLOAT)')
    c.close()
    
    conn = sqlite3.connect('./db/okcoin_ltc_usd.db', check_same_thread=False)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS data (name STR, timestamp INT, price FLOAT, v_bid FLOAT, v_ask FLOAT)')
    c.close()
    


def add(name,timestamp,price,v_bid,v_ask):
    conn = sqlite3.connect('./db/'+name+'.db', check_same_thread=False)
    c = conn.cursor()
    c.execute("INSERT INTO data VALUES(?,?,?,?,?)",(name,timestamp,price,v_bid,v_ask))
    conn.commit()
    conn.close()


