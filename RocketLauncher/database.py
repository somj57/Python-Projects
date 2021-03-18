import mysql.connector

class database():
    def __init__(self):
        #Connecting with database
        self.dbConnection = mysql.connector.connect(host = "localhost",user = 'somya',password = 'somya',database = 'records' ) 
        # print("Connecting to database")
        self.cursor = self.dbConnection.cursor()
        # print("Database connection was successful")
    
    def fetchData(self):
        '''
        This method will fetch the data from the database
        '''
        query1 = "SELECT * FROM rocket"
        try:
            self.cursor.execute(query1)
            result = self.cursor.fetchall()
            return result
        except mysql.connector.Error as error:
            self.dbConnection.rollback()
            return f"Failed featching record into interns...\n{error}"
        finally:
            if(self.dbConnection.is_connected()):
                self.cursor.close()
                self.dbConnection.close()
                # return "Data not found"


# UPDATE `rocket` SET `Netlinks`=1,`Fuel`=1,`Power`=1,`Oxygen`=1,`EngineOn`=1 
# UPDATE `rocket` SET `Netlinks`=0,`Fuel`=0,`Power`=0,`Oxygen`=0,`EngineOn`=0 