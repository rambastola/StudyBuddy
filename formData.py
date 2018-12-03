from flask import Flask, render_template, request
from connect import *
import pickle

app = Flask(__name__)


@app.route('/')
def mainPage():
    return render_template('index.html')

@app.route('/signup')
def entertext():
    return render_template("signup.html")

@app.route('/data', methods=['GET','POST'])
def signupData():
    if request.method =='POST':
        name = request.form['Username']
        email = request.form['email']
        password = request.form['password']
        uploadonDB(name, email, password)
        return render_template('login.html')

    else:
        return render_template('signup.html')

# @app.route('/getloginData')
# def loginx():
#     return render_template('login.html')
@app.route('/login', methods=['GET','POST'])
@app.route('/login')
def login():
     if request.method =='POST':
         name = request.form['Username']
         password = request.form['password']
     return render_template('mainpage.html')



if __name__ == '__main__':
    app.run(debug=True)
