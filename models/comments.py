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

def show_all_comments():
    all_comments = sql_read("SELECT user_name, comment_content FROM users JOIN comments ON users.user_id = comments.comment_author_id;;")
    print(all_comments)
    return all_comments

def edit_comment(comment_content, comment_id):
    sql_write("UPDATE comments SET comment_content = %s WHERE comment_id = %s;", [comment_content, comment_id])
    print("it worked")
    return

def delete_comment(comment_id):
    
    sql_write("DELETE FROM comments WHERE comment_id =%s;", [comment_id])
    print("comment deleted")
    return True

def get_user(username):
    query = sql_read("SELECT * FROM users WHERE user_name=%s;", [username])
    user_info = query[0]
    return user_info

def get_single_comment(comment_id): 
    content_to_edit = sql_read("SELECT comment_content FROM comments WHERE comment_id=%s",[comment_id] )
    comment_string = content_to_edit[0][0]
    print(comment_string)
    return comment_string


# insert_comment("Ron", "hey hey")
# show_user_comments("Harry")
# get_user("Harry")
# delete_comment(12)
# show_all_comments()

# get_single_comment(13)
# edit_comment("hello this is edited comment1", 13)