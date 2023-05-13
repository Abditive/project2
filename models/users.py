import psycopg2
import os
import bcrypt


def sql_read(read_query, parameters =[]):
    connection = psycopg2.connect(os.getenv("DATABASE_URL"))
    cursor = connection.cursor()
    cursor.execute(read_query, parameters)
    query_results = cursor.fetchall()
    connection.commit()
    connection.close()
    return query_results


def sql_write(write_query, parameters = []):
    connection = psycopg2.connect(os.getenv("DATABASE_URL"))
    cursor = connection.cursor()
    cursor.execute(write_query, parameters)
    connection.commit()
    connection.close()
    return


def create_user(username, email, password):
    if check_user(username, email):
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        sql_write("INSERT INTO users (user_name, user_email, user_password) VALUES (%s, %s, %s);", [username.lower(), email.lower() ,hashed_password])
        print("user created")
        return True
    else:
        print("user could not be created. username or email already exist")
        return False

def check_user(username, email):
  
    user__check_query = f"SELECT user_name, user_email from users WHERE user_email='{email}';"
    user_check_results = sql_read(user__check_query)
    if user_check_results != []:
        print('this email address is associated with an existing account')
        return False
    else:
        print("email address does not exist yet")
        user_check_username = f"SELECT user_name  from users WHERE user_name='{username}';"
        if sql_read(user_check_username) !=[]:
            print("this usermane is taken. Try a different one")
            return False
        else: 
            
            return True 

def log_in_user(username, password):
    log_in_result = sql_read("SELECT * FROM users WHERE user_name = %s;", [username])
    if log_in_result !=[]:
        user = log_in_result[0]
        hashed_pw = user[3]
        if bcrypt.checkpw(password.encode(), hashed_pw.encode()):
            print("success")
            return user
        else:
            print("invalid username or password 22")
            return False
    else:
        print("invalid username or password1")
        return False
    
def show_user_profile(username):
    query = sql_read("SELECT user_name, user_email FROM users WHERE user_name = %s;", [username])
    print(query[0])
    return query[0]


# create_user("Dexter", "bestdog@gmail.com", "123")
# log_in_user("Harry", "0000")
