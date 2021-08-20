from flask import Flask,jsonify,render_template,request


app = Flask(__name__)

@app.route('/users/<int:userid>')
def getUser(userid):
    try:
        print(userid)
        output=("hello world")
        return (output)
        
    except Exception as err:
        print(err)
        return {},500

if __name__ == '__main__':
    app.run(port=8081,debug=True) 