import MySQLdb
res=MySQLdb.connect("localhost","root","Rajneha#123","Acadview2")
cursor=res.cursor()
def add(tit,auth,yea,isb):
    prt=("INSERT INTO Book2(Title,Author,Year1,Isbn) VALUES ('%s', '%s', '%d', '%d')" % (tit, auth, yea, isb))
    cursor.execute(prt)
    res.commit()
def view():
    prt1="SELECT * FROM Book2"
    cursor.execute(prt1)
    result=cursor.fetchall()
    for i in result:
       print(i)
def search(yea):
   prt2=("SELECT * FROM Book2 WHERE Isbn = '%d'" % yea)
   cursor.execute(prt2)
   result1=cursor.fetchone()
   print(result1)
def delete(yea1):
   prt3=("DELETE FROM Book2 WHERE Title = '%s'" % yea1)
   cursor.execute(prt3)
   res.commit()
add("who ishubham raj","nea rahman",207,178)
search(2008)
delete("prtp ")
view()
res.close()


