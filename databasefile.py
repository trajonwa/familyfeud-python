import mysql.connector
from mysql.connector import Error

def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

connection = create_server_connection("localhost", "root", "root")


# create_database_query="CREATE DATABASE questionnaire"
# create_database(connection, create_database_query)



create_questionnare = """
CREATE TABLE questionnare (
  question_id INT PRIMARY KEY, 
  Question VARCHAR(255) NOT NULL, 
  answer_1 VARCHAR(40) NOT NULL, 
  answer_2 VARCHAR(40) NOT NULL, 
  answer_3 VARCHAR(40) NOT NULL,
  answer_4 VARCHAR(40) NOT NULL, 
  answer_5 VARCHAR(40) NOT NULL, 
  answer_6 VARCHAR(40) NOT NULL,
  answer_7 VARCHAR(40) NOT NULL, 
  answer_8 VARCHAR(40) NOT NULL 
); """

connection = create_db_connection("localhost", "root", "root", "questionnare") # Connect to the Database
# execute_query(connection, create_questionnare) # Execute our defined query
'''
create_answers = """
CREATE TABLE answers (
  answer INT PRIMARY KEY, 
  similar_answer_1 VARCHAR(40) NOT NULL, 
  similar_answer_2 VARCHAR(40) NOT NULL, 
  similar_answer_3 VARCHAR(40) NOT NULL
);
"""
connection = create_db_connection("localhost", "root", "HOST1234", "questionare") # Connect to the Database
execute_query(connection, create_answers) # Execute our defined query
'''