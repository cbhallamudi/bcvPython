import newPkg.dbConnection

while True:
    userInput = input("Press 'at' to get all the tables in the database\n'gtd' to get data from a table\n anything else to break the operation: \n")
    if userInput == 'at':
        newPkg.dbConnection.getTables()
    elif userInput == 'gtd':
        newPkg.dbConnection.getTableData()
    else:
        break    