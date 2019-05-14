import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="pythonDb"
)
mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE pythonDb")
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#   print(x) 
# mycursor.execute("CREATE TABLE tbl_users (name varchar(100),username varchar(255),password varchar(200),email varchar(255) )")
mycursor.execute("drop table tbl_users")
mycursor.execute("show tables")
for x in mycursor:
  print(x)