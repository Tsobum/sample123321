import os
class Settings:
    secretKey="a12nc)238OmPq#cxOlm*a"

    #Dev
    #host='ohunm00fjsjs1uzy.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
    #database='f00hizbmcwoco2jn'
    #user='lmgmdwmouzlv0vt9'
    #password='ij8nhoj7vno27h15'

    #Production
    host=os.environ['Host']
    database='f00hizbmcwoco2jn'
    user=os.environ['Username']
    password=os.environ['Password']

    #DEV2TESTLOCAL
    #host='localhost'
    #database='f00hizbmcwoco2jn'
    #user='root'
    #password='root'
