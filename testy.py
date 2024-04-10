import mysql.connector
from flask import *
from flask_mail import *
from random import randint
'''
SHOULD INTEGRATE TWO FLASK APPS STILL 
SHOULD IMPLEMENT CODE FOR EMAIL VERIFICATION TO BE CONTINUED 
'''
app = Flask(__name__)
app.secret_key = "i_am_ironman"
@app.route("/")
def head():
    return render_template("preview.html")
def fetchDetails(name):
    user_database = mysql.connector.connect(host="localhost",user="root",passwd="Harsha@2004",database ="users")
    cursor=user_database.cursor()
    cursor.execute("SELECT * FROM user_details")
    names_list = [ i[0] for i in cursor ]
    user_database.close()
    if name in names_list:
        return True
    return False 
def fetchPasswd(uname,paswd):
    user_database = mysql.connector.connect(host="localhost",user="root",passwd="Harsha@2004",database ="users")
    cursor=user_database.cursor()
    cursor.execute("SELECT * FROM user_details")
    names_list = [ (i[0],i[1]) for i in cursor ]
    user_database.close()
    for i in names_list:
        if i[0]==uname and i[1] == paswd:
            return True
    return False
@app.route("/login",methods = ["POST","GET"])
#Login page details were completed
def login():
  if request.method=='POST':
    uname = request.form["Uname"]
    passwd = request.form["Passwd"]
    if not uname or not passwd:
        return "Enter the valid details"
    if fetchDetails(uname):
        if fetchPasswd(uname,passwd):
            return render_template("index.html")
        return "wrong_password"
    return "no_user_name_found"
@app.route("/sign-up",methods = ["POST","GET"])
def signUp():
    return render_template("view.html")
@app.route("/sign-Up-Details",methods=["POST","GET"])
def signupDetails():
  if request.method=='POST':
    uname = request.form["user_name"]
    password = request.form["pass"]
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    email = request.form["email"]
    if not uname or not password or not first_name or not last_name or not email:
        return "Enter the valid details"
    if saveDetailsIntoDatabase(uname , password ,first_name ,last_name ,email):
        return redirect(url_for('index'))
    return redirect(url_for("signUp"))
def saveDetailsIntoDatabase(name , password , firstname , lastname , email):
    connectivity = mysql.connector.connect(host='localhost',user='root',passwd = "Harsha@2004",database='users')
    try:
       cursor = connectivity.cursor()
       cursor.execute("INSERT INTO user_details VALUES (%s,%s,%s,%s,%s)",(name,password,firstname,lastname,email))
       connectivity.commit()
       return True 
    except:
       connectivity.close()
    return False
if __name__ == '__main__':
    app.run(debug=True)
    
