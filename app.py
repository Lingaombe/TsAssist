from flask import Flask, render_template, request, jsonify
import mysql.connector
conn = mysql.connector.connect(host="localhost", user="root", password="Lingaombe@2001", database="TsAssist") 

if conn.is_connected():
    print("Successfully connected to the database")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/signup", methods=["GET"])
def signup():
    return render_template("signup.html")

@app.route("/signin", methods=["GET"])
def signin():
    return render_template("signin.html")

@app.route('/signupData', methods=['POST'])
def signupData():

    # Get the form data as Python ImmutableDict datatype 
    data = request.form
    userName = data['fullname'],
    userEmail = data['email'],
    userPassword = data['password'],

    cursor = conn.cursor()
    sql = "INSERT INTO users (userName, userPassword, userEmail) VALUES (%s, %s, %s)"
    val = (userName, userPassword, userEmail)
    cursor.executemany("INSERT INTO users (userName, userPassword, userEmail) VALUES (%s, %s, %s);", (userName, userPassword, userEmail))
    conn.commit()
    cursor.close()
    return render_template("index.html", userName=userName)    

@app.route("/PaperGen", methods=['GET'])
def paperGen():
    return render_template("paperGen.html")

@app.route("/getTables", methods=['GET'])
def getTables():
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    cursor.close()
    tableNames = [t[0] for t in tables]
    return jsonify({"tables":tableNames}), 200

@app.errorhandler(404)
def page_not_found(error):
    # Return a custom 404 error page
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)