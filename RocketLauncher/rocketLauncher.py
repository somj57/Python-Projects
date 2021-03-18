# Importing packages
from database import *

class rocket(database):
    '''
    This class is acting like a middle class for our concrete class to interect with 
    '''
    def __init__(self):
        '''
        This function will create the connection to the database and will fetch all the data from the database
        '''
        super().__init__()
        self.data = super().fetchData()
        # print(self.data)
    
    def checkData(self,i):
        '''
        This function will return the data of the requested state
        '''
        # print(self.data)
        return self.data[0][i]

























'''
import mysql.connector

class database():
    def __init__(self):
        #Connecting with database
        self.dbConnection = mysql.connector.connect(host = "localhost",user = 'somya',password = 'somya',database = 'records' ) 
        print("Connecting to database")
        self.cursor = self.dbConnection.cursor()
        print("Database connection was successful")
    
    def fetchData(self):
        query1 = "SELECT * FROM rocket"
        try:
            self.cursor.execute(query1)
            result = self.cursor.fetchall()
            # result = cursor.fetchone() # TO fetch only frist value in the table
            for data in result:
                print(data)
        except mysql.connector.Error as error:
            self.dbConnection.rollback()
            print(f"Failed featching record into interns...\n{error}")
        finally:
            if(self.dbConnection.is_connected()):
                self.cursor.close()
                self.dbConnection.close()
                print("MySql connection is closed!...")
'''