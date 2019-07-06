from tkinter import *
import mysql.connector
from ItemClass import Item

class inventoryConnection:
    mydb = ""
    queryText = ""
    def __init__(self, newHost, newDataBase, newUser, newPassword):
        self.mydb = mysql.connector.connect(
        host = newHost,
        database = newDataBase,
        user = newUser,
        password = newPassword,
        )

    def query(self, queryText, needsReturning):
        myCursor = self.mydb.cursor()
        myCursor.execute(queryText)
        if(needsReturning): #if data needs to be returned, like with
            result = myCursor.fetchall() #'select * from ...;'
            print(result)
            return result

    def closeConnection(self):
        myCursor.close()
        self.mydb.close()

    def addItem(self, Item, tableName):
        queryText = ('insert into %s values ((%d), (%s), (%d), (%d), (%s), (%s));' % (tableName,Item.getID(), Item.getName(), Item.getCost(), Item.getPrice(), Item.getShelfLife(), Item.getDateEntered()))
        print(queryText)
        self.query(queryText, False)

    def selectItems(self, tableName, condition):
        queryText = 'select * from %s' %(tableName)
        if(condition is not None): #for example: you want to add "where id = 5"
            queryText = queryText + ' ' + condition
        queryText = queryText + ';'
        #print(queryText)
        return self.query(queryText, True)
