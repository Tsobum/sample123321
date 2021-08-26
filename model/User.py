from model.DatabasePool import DatabasePool

class log_User:

#    @classmethod
#    def getUsers(cls,userid):
#        try:
#            dbConn=DatabasePool.getConnection()
#            cursor = dbConn.cursor(dictionary=True)

#            sql="select * from user where userid=%s"
#            cursor.execute(sql)
#            users=cursor.fetchall()
#            return users
#        finally:
#            dbConn.close()

    @classmethod
    def loginUser(cls,email,password):
        try:
            dbConn=DatabasePool.getConnection()
            cursor = dbConn.cursor(dictionary=True)

            sql="select * from users where email=%s and password=%s"
            cursor.execute(sql,(email,password))
            users=cursor.fetchone()
            return users

        finally:
            dbConn.close()
    