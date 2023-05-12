from flask import Flask, render_template, request, redirect, session 
from models import users
import os
import psycopg2
import bcrypt

app = Flask(__name__)
secret_key = os.getenv("SECRET_KEY")
app.config["SECRET_KEY"] = secret_key

@app.route('/')
def index(): 
    if session.get("user_id", ""):
        show_user = session["user_id"]
    else:
        show_user = "guest"
    return render_template("home.html", logged_user = show_user)
#     connection = psycopg2.connect(host=os.getenv("PGHOST"), user=os.getenv("PGUSER"), password=os.getenv("PGPASSWORD"), port=os.getenv("PGPORT"), dbname=os.getenv("PGDATABASE"))
     # connection = psycopg2.connect(os.getenv("DATABASE_URL"))
#     cursor = connection.cursor()
#     cursor.execute("SELECT * FROM mytable;")
#     results = cursor.fetchall()
#     connection.close()
#     return f"{results[0]}"

# if __name__ == '__main__':
#     app.run(debug=True, port=os.getenv("PORT", default=5000))

@app.route('/form/signup')

def sign_up_form():

    return render_template("sign_up_form.html")

@app.route('/api/form/signup', methods = ["POST"])

def sign_up():

    # NEED TO ADD check for existing email and usernames
    new_username = request.form.get("username")
    new_email = request.form.get("email")
    new_password = request.form.get("password")
    if users.create_user(new_username, new_email, new_password):
        return render_template("profile.html")
    else:
        return "User could not be created. Try Again"


@app.route('/form/login')

def log_in_form():
    
    return render_template("login_form.html")

@app.route('/api/form/login', methods = ["POST"])

def log_in():
    username = request.form.get("username")
    password = request.form.get("password")
    user_data = users.log_in_user(username, password)
    # print(user_data[1])
    if user_data:
        session["user_id"] = user_data[1]
        return redirect('/')
    else:
        
        return "Could not login, try again"    
    
@app.route('/logout')
def log_out():
    session.clear()
    return redirect('/')

app.run(debug=True)