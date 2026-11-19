import mysql.connector as db;
con=db.connect(user="root",password="vighnesh21V",host="localhost",database="train_booking");
print(con)
cur=con.cursor()
cur.excute("select * from trains")
data=cur.fetchall()
con.close()