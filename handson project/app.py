from flask import Flask, render_template, request, redirect, url_for, session,jsonify
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re


app = Flask(__name__)


app.secret_key = 'your secret key'


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'project'

mysql = MySQL(app)


@app.route('/')
def hello():
    return'hello world'

@app.route('/reg',methods=['POST','GET'])
def reg():
    if request.method=='POST':
        name=request.form["name"]
        email=request.form["email"]
        mobno=request.form["mobno"]
        address=request.form["address"]
        
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO project (name, email, mobno, address) VALUES (%s, %s, %s, %s)",(name, email, mobno, address))
        mysql.connection.commit()
        cur.close()
        
        return jsonify("registered")
    return jsonify("registered")

if __name__ == "__main__":
	app.run()
