import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
    user = 'root',
    password = 'kwaku12345',
)
   


cursorObject = dataBase.cursor()


cursorObject.execute('CREATE DATABASE kwakudb')

print("All done!")