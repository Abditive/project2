import psycopg2
import os
import bcrypt
import users

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
    get_user_info = users.get_user(username)
    print(get_user_info[0])
    sql_write("INSERT INTO comments (comment_author_id, comment_content) VALUES (%s, %s);", [get_user_info[0], content])    
    return print("success")

def edit_comment():
    return

def delete_comment():
    return


insert_comment("Ron", "hey hey")