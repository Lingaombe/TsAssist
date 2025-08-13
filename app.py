from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=["GET"])
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

    ## Return the extracted information 
    return {
        'fullName': data['fullname'],
        'email': data['email'],
        'password': data['password'],
        'confirmPassword': data['confirm_password']
    }

@app.route("/PaperGen", methods=['GET'])
def paperGen():
    return render_template("paperGen.html")

@app.errorhandler(404)
def page_not_found(error):
    # Return a custom 404 error page
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)