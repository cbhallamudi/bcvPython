import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="mydatabase"
)
mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE mydatabase")
# mycursor.execute("SHOW DATABASES")
# mycursor.execute("CREATE TABLE users(id int(11) AUTO_INCREMENT PRIMARY KEY,name varchar(100),password varchar(250))")
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#   print(x)
name,password = input("Enter Name: "),input("Enter Password: ")
data = (name,password)
mycursor.execute("INSERT INTO users(name,password) VALUES(%s,%s)",data)
mydb.commit()
