from model.DatabasePool import DatabasePool
from config.Settings import Settings

class User:

    @classmethod
    def getUser(cls,userid):
        try:
            dbConn=DatabasePool.getConnection()
            #db_Info = dbConn.connection_id
            #print(f"Connected to {db_Info}");

            cursor = dbConn.cursor(dictionary=True)
            sql="select * from users where userid=%s"

            cursor.execute(sql,(userid,))
            users = cursor.fetchall() 

            return users

        finally:
            dbConn.close()
            print("release connection")


