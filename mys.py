import sqlite3 as lite
con =lite.connect('bio.db')
cur=con.cursor()
def select():
    sql="CREATE TABLE if not exists doctor (id STRING PRIMARY KEY," \
    "name STRING NOT NULL," \
    "password STRING NOT NULL)"
    cur.execute(sql)
    con.commit()
    return cur
def insert( docid , name , password ):
    sql="insert into doctor values (?, ? ,?)"
    val=(docid , name, password)
    cur.execute(sql,val)
    con.commit()
def validate(docid ,password):
    sql="select password from doctor where id=?"
    cur.execute("select * from doctor")
    rows=cur.fetchall()
    print(rows)
    adr=(docid,)
    cur.execute(sql,adr)
    myresult = cur.fetchone()
    print(myresult)
    if myresult != None:
        if myresult[0] == password :
            return True
    else:
        return False