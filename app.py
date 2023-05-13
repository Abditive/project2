from flask import Flask, render_template, request, redirect, session 
from models import users, comments
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
    all_comments=comments.show_all_comments()

    return render_template("home.html", login_user = show_user, comment_info = all_comments)

@app.route('/form/signup')

def sign_up_form():
    
    return render_template("sign_up_form.html")

@app.route('/api/form/signup', methods = ["POST"])

def sign_up():

    new_username = request.form.get("username")
    new_email = request.form.get("email")
    new_password = request.form.get("password")
    if users.create_user(new_username, new_email, new_password):
        return redirect('/')
    else:
        return redirect('/')


@app.route('/form/login')

def log_in_form():
    
    return render_template("login_form.html")

@app.route('/api/form/login', methods = ["POST"])

def log_in():
    username = request.form.get("username")
    password = request.form.get("password")
    user_data = users.log_in_user(username, password)
    
    if user_data:
        session["user_id"] = user_data[1]
        return redirect('/')
    else:
        
        return redirect('/form/login')  
    
@app.route('/<user>/profile')
def show_profile(user):
    if session.get("user_id"):
        user_info =users.show_user_profile(user)
        user_comments=comments.show_user_comments(user)
        return render_template('profile.html', user_information = user_info, user_c=user_comments)
    else:
        return "access denied"

@app.route('/logout')
def log_out():
    session.clear()
    return redirect('/')

@app.route('/<user>/create/comment')
def create_comment_form(user):
    if session.get("user_id"):
        return render_template('create_comment.html', comment_author = user)
    else:
        return "access denied"
    
@app.route('/api/<user>/create/comment', methods = ["POST"])
def create_new_comment(user):
    new_comment = request.form.get("comment")
    comments.insert_comment(user,new_comment)
    return redirect(f'/{user}/profile')



@app.route('/api/<user>/<comment_id>/delete', methods = ["POST"])
def delete_comment(user, comment_id):
    comments.delete_comment(comment_id)
    return redirect(f'/{user}/profile')

@app.route('/<user>/<comment_id>/edit', methods = ["POST"])
def edit_comment_form(user,comment_id):
    comment_str = comments.get_single_comment(comment_id)
    return render_template("edit_comment.html", comment_author=user, id_comment = comment_id, comment_string = comment_str)

@app.route('/api/<user>/<comment_id>/edit', methods = ["POST"])
def edit_comment(user,comment_id):
    edited_comment =request.form.get("comment")
    comments.edit_comment(edited_comment,comment_id)
    return redirect(f'/{user}/profile')


if __name__ == "__main__":
    app.run(debug=True)