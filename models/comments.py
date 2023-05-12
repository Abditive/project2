import psycopg2
import os
import bcrypt

def sql_read(read_query, parameters =[]):
    connection = psycopg2.connect(
        "dbname = communio_app user = postgres password=Dexter#2020")
    cursor = connection.cursor()
    cursor.execute(read_query, parameters)
    query_results = cursor.fetchall()
    connection.commit()
    connection.close()
    return query_results


def sql_write(write_query, parameters = []):
    connection = psycopg2.connect(
        "dbname = communio_app user = postgres password=Dexter#2020")
    cursor = connection.cursor()
    cursor.execute(write_query, parameters)
    connection.commit()
    connection.close()
    return

def insert_comment(username, content):
    get_user_info = get_user(username)
    print(get_user_info[0])
    sql_write("INSERT INTO comments (comment_author_id, comment_content) VALUES (%s, %s);", [get_user_info[0], content])    
    
    return 

def show_user_comments(username):
    get_user_info = get_user(username)
    print(get_user_info[0])
    get_comments =sql_read("SELECT * FROM comments WHERE comment_author_id =%s", [get_user_info[0]])   
    return get_comments

def edit_comment():
    return

def delete_comment():
    return

def get_user(username):
    query = sql_read("SELECT * FROM users WHERE user_name=%s;", [username])
    user_info = query[0]
    return user_info


# insert_comment("Ron", "hey hey")
show_user_comments("Harry")
# get_user("Harry")