import mysql.connector as mysql

dbConnection  = mysql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'mydatabase'
)

dbHandler = dbConnection.cursor()

def getTables():
    dbHandler.execute('SHOW TABLES')
    print("Tables in the Database: ")
    for x in dbHandler:
        print(x)
def getTableData():
    
    tblName = input('Enter Table Name: ')
    dbHandler.execute('SELECT * FROM '+str(tblName))
    myresult = dbHandler.fetchall()
    for x in myresult:
        print(x)
