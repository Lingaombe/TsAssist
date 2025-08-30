from flask import *

import secrets
secretKey = secrets.token_hex(16) # osapanga deploy
import csv, uuid

import mysql.connector
conn = mysql.connector.connect(host="localhost", user="root", password="Lingaombe@2001", database="TsAssist") 

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
    response = make_response(render_template("userIn.html", userName=userName))
    response.set_cookie("userName", userName)
    return response  

################################################### 404 NOT FOUND ###################################################

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

################################################### PAPER GEN ###################################################


@app.route("/PaperGenReq", methods=['GET'])
def PaperGenReq():
    return render_template("PaperGenReq.html")

DB = {"papers": {}}

@app.route("/upload", methods=["GET", "POST"])
def upload_csv():
    if request.method == "POST":
        file = request.files["csv_file"]
        paper_id = str(uuid.uuid4())
        paper = {"id": paper_id, "sections": {}}

        reader = csv.DictReader(file.stream.read().decode("utf-8").splitlines())
        for row in reader:
            sec_name = row["section"].strip()
            if sec_name not in paper["sections"]:
                paper["sections"][sec_name] = {"name": sec_name, "questions": []}

            q = {
                "id": str(uuid.uuid4()),
                "type": row["type"],
                "text": row["question"],
                "marks": int(row["marks"]),
                "difficulty": row.get("difficulty"),
                "bloom": row.get("bloom"),
                "tags": row.get("tags", "").split(";"),
                "options": [row.get("option_a"), row.get("option_b"), row.get("option_c"), row.get("option_d")],
                "answer": row.get("answer") or row.get("correct")
            }
            paper["sections"][sec_name]["questions"].append(q)

        DB["papers"][paper_id] = paper
        return redirect(url_for("preview_paper", paper_id=paper_id))

    return render_template("upload.html")

@app.route("/papers/<paper_id>/preview")
def preview_paper(paper_id):
    paper = DB["papers"][paper_id]
    return render_template("preview.html", paper=paper)

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