from flask import Flask,jsonify,render_template,request
from model.User import User

app = Flask(__name__)

@app.route('/users/<int:userid>')
def getUser(userid):
    try:
        #print(g.userid)
        jsonUsers=User.getUser(userid)
        jsonUsers={"Users":jsonUsers}
        print("jsonusers",jsonUsers)
        return jsonify(jsonUsers),200
    except Exception as err:
        print(err)
        return {},500

if __name__ == '__main__':
    app.run(port=8081,debug=True) 