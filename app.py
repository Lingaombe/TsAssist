from flask import *
import pandas as pd

from ollamafreeapi import OllamaFreeAPI
client = OllamaFreeAPI()

import secrets
secretKey = secrets.token_hex(16) # osapanga deploy
import csv, uuid

import mysql.connector
conn = mysql.connector.connect(host="localhost", user="root", password="Lingaombe@2001", database="TsAssist") 
cursor = conn.cursor()

if conn.is_connected():
    print("Successfully connected to the database")

app = Flask(__name__)
app.secret_key = secretKey 

@app.route("/")
def home():
    return render_template("index.html")

################################################### SIGNUP/LOGIN ###################################################

@app.route("/signin", methods=["GET"])
def signin():
    return render_template("signin.html")

@app.route("/signedin", methods=["POST"])
def signedin():
    userEmail = request.form['email']
    userPassword = request.form['password']
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE userEmail = %s AND userPassword = %s", (userEmail, userPassword))
    user = cursor.fetchone()
    # ngati password ndi email zili mu database
    if user:
        return render_template("userIn.html", userName=user[1]) #user atuluka list nde indexing kutengera ma column
    else:
        # ngati email yokha ili mu database, password yolakwika
        cursor.execute("SELECT * FROM users WHERE userEmail = %s", (userEmail,))
        userExists = cursor.fetchone()
        if userExists:  
            flash('Login unsuccessful, check your password and try again.', 'error')
            return render_template("signin.html")
        # munthu alembetse
        else:
            flash('User does not exist, please sign up!')
            return render_template("signup.html")

@app.route("/signup", methods=["GET"])
def signup():
    return render_template("signup.html")

@app.route('/signupData', methods=['POST'])
def signupData():
    # kutenga formData kuchoka ku signup.html 
    data = request.form
    userName = data['fullname']
    userRole = data['role']
    userEmail = data['email']
    userPassword = data['password']

    cursor = conn.cursor()
    sql = "INSERT INTO users (userName, userRole, userPassword, userEmail) VALUES (%s, %s, %s, %s);"
    val = (userName, userRole, userPassword, userEmail)
    cursor.execute(sql, val)
    conn.commit()
    cursor.close()
    response = make_response(render_template("userIn.html", userName=userName)) #kusunga ma cookies
    response.set_cookie("userName", userName)
    return response  

################################################### MISCILLANEOUS ###################################################

@app.route("/settings")
def settings():
    username = request.cookies.get('userName') 

    return render_template("userSettings.html", userName=username)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

################################################### PAPER GEN ###################################################

class Paper:
    def __init__(self, schoolName, totalMarks, instructions):
        # self.schoolLogo = schoolLogo
        self.schoolName = schoolName
        self.totalMarks = totalMarks
        self.instructions = instructions

@app.route("/paperDetails", methods=['POST'])
def paperDetails():
    # logo = request.form['logo']
    schoolName = request.form['schoolName']
    marks = request.form['totalMarks']
    instructions = request.form['instructions']

    paper = Paper(schoolName, marks, instructions)
    print(paper.schoolName)
    flash('Details added successfully!')
    return render_template("PaperGenReq.html")
    
@app.route("/PaperGenReq", methods=['GET'])
def PaperGenReq():
    return render_template("PaperGenReq.html")

@app.route("/papers/<paper_id>/preview")
def preview_paper(paper_id):
    cursor = conn.cursor(dictionary=True)  
    cursor.execute("SELECT * FROM papers WHERE id = %s", (paper_id,))
    paper = cursor.fetchone()
    cursor.close()

    if not paper:
        abort(404, description="Paper not found")

    return render_template("preview.html", paper=paper)

################################################### GEN ONE

@app.route("/bankPaperGen", methods=['GET', 'POST'])
def bankPaperGen(): 
    data = request.form
    file = data['fullname']
    file_path = 'your_file.xls'

################################################### GEN TWO

@app.route("/addQuestion", methods=['POST'])
def addQuestion():
    data = {
    "paperName" : request.form['paperName'],
    "questionType" : request.form['questionType'],
    "questionMarks" : request.form['questionMarks'],
    }

    cursor = conn.cursor()
    sql = "INSERT INTO questions (paperName, questionType, questionMarks) VALUES (%s, %s, %s);"
    val = (data["paperName"], data["questionType"], data["questionMarks"])
    cursor.execute(sql, val)
    if cursor.rowcount > 0:
        flash('Question Added Successful!', "success") #ngati funso laikidwa mu db
    else:
        flash('Question Not Added!', "error") #ngati funso silinaikidwe mu db

    conn.commit()
    cursor.close()

    return render_template("PaperGenReq.html")

@app.route("/manualPaperGen", methods=['POST'])
def manualPaperGen():
    paperDetails() #returns paper object with attrs logo, name, subject, name, marks, ins
    totalMarks = paper.totalMarks

    return redirect(url_for('preview_paper', data=data))

################################################## GEN THREE

# Get instant responses
# response = client.chat(
#     model_name="llama3.3:70b",
#     prompt="Explain hugs like I'm five",
#     temperature=0.7
# )
# print(response)

################################################### DATABASE GETS ###################################################

@app.route("/getTables", methods=['GET'])
def getTables():
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    cursor.close()
    tableNames = [t[0] for t in tables]
    return jsonify({"tables":tableNames}), 200


if __name__ == "__main__":
    app.run(debug=True)