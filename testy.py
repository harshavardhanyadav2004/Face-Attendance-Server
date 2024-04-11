
import mysql.connector
from flask import *
from flask_mail import *
from random import randint
from video_preprocess import video_preprocessing
from MainCode import *
from main_class import face_recog
'''
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
@app.route('/video-upload')
def index():
    return render_template('index.html')

ALLOWED_EXTENSIONS = ['mp4']

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/upload",methods = ['POST'])
def upload():
    if 'video' not in request.files:
        return "NO video File found"
    video = request.files['video']
    if video.filename == "":
        return "NO video file selected"
    if video and allowed_file(video.filename):
        video.save('static/videos/' + video.filename)
        if video_preprocessing.empty_folder():
            if video_preprocessing.extract_frames_per_second():
                images_paths = face_recog.load_image_paths()
                final_face = face_recog.find_faces(images_paths)
                attendees_list = face_recog.compare_faces(final_face)
                return render_template("names.html")
            return video_preprocessing.string
        else:
            return "<h1> Error in the Folder<h1>"
    return "inavalid file type"
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
    if not uname or not passwd :
        return "Enter the valid details"
    if fetchDetails(uname):
        if fetchPasswd(uname,passwd):
          return redirect(url_for("index"))
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
        return redirect(url_for("index"))
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
#SignUP Details Completed 
if __name__ == '__main__':
    app.run(debug=True)
    