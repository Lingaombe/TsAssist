from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/signUp", methods=["GET"])
def signUp():
    return render_template("signup.html")

@app.route('/signup', methods=['POST'])
def signup():

    # Get the form data as Python ImmutableDict datatype 
    data = request.form

    ## Return the extracted information 
    return {
        'fullName': data['fullname'],
        'email': data['email'],
        'password': data['password'],
        'confirmPassword': data['confirm_password']
    }

@app.errorhandler(404)
def page_not_found(error):
    # Return a custom 404 error page
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)