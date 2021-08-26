from flask import Flask,jsonify,render_template,request
from model.DatabasePool import DatabasePool
import os
from mysql.connector import pooling


app = Flask(__name__)

#@app.route('/users/<int:userid>')
#def getUser(userid):
#    try:
#        #print(g.userid)
#        jsonUsers=User.getUser(userid)
#        jsonUsers={"Users":jsonUsers}
#        print("jsonusers",jsonUsers)
#        return jsonify(jsonUsers),200
#    except Exception as err:
#        print(err)
#        return {},500

@app.route('/login')
def form():
    return render_template("login.html",message="Please Log In")

@app.route('/verifyUser', methods=['POST'])
def verifyUser():

        email = request.form['email']
        password = request.form['password']

        dbConn=DatabasePool.getConnection()
        cursor = dbConn.cursor(dictionary=True)

        sql="select * from users where email=%s and password=%s"
        cursor.execute(sql,(email,password))
        users=cursor.fetchone()
        print(users)
     
        if users is None:
            return render_template('login.html',message="Invalid Log In")

        else:
           #data = []
           #index = []
           #for i in range (1,6):
                #index.append(i)
                #data.append(i*5)   

        #arrofobj =dict(zip(index,data))
            return render_template('mainPage.html',message="Welcome", name=users['name'],arrofobj=[{"index":1, "data":"5"},{"index":2,"data":"10"},{"index":3,"data":"15"},{"index":4,"data":"20"},{"index":5,"data":"25"}])      


if __name__ == '__main__':
    app.run(debug=True) 