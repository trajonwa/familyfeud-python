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


# create_database_query="CREATE DATABASE questionnaire"
# create_database(connection, create_database_query)



def create_tables():

    create_questionnare = """
    CREATE TABLE questionnare (
    question_id INT PRIMARY KEY,
    question VARCHAR(255) NOT NULL
    ); 
    """

    create_answers = """
    CREATE TABLE answers (
    answer_id INT, 
    question_id INT NOT NULL, 
    answer VARCHAR(100) NOT NULL, 
    multiple_answers BIT(1) NOT NULL,
    PRIMARY KEY(answer_id, question_id),
    FOREIGN KEY(question_id) REFERENCES questionnare(question_id) ON DELETE CASCADE

    );
    """

    create_score = """
    CREATE TABLE score (
    score_id INT,
    answer_id INT NOT NULL,
    score INT NOT NULL,
    PRIMARY KEY(score_id, answer_id),
    FOREIGN KEY(answer_id) REFERENCES answers(answer_id) ON DELETE CASCADE
    
    );
    """

    pw = input("Please enter password to access FamilyFeud Database: ")
    db = str(input("Please specify database you'd like to connect to: "))

    connection = create_db_connection("localhost", "odos", pw, db)
    execute_query(connection, create_questionnare)
    execute_query(connection, create_answers)
    execute_query(connection, create_score)

def fill_initial_data():
    
    pop_questionnare = """
    INSERT INTO questionnare VALUES
    (1, "Name a reason you might get rid of an old family heirloom."),
    (2, "Where do kids nowadays spend most of their time?"), 
    (3, "Tell me something many people do just once a week.");
    """

    pop_answers = """
    INSERT INTO answers VALUES
    (1, 1, "Broken", 0),
    (2, 1, "Ugly", 0), 
    (3, 1, "Divorce", 0),
    (4, 1, "Sell/need money", 1),
    (5, 1, "Too much stuff", 0), 
    (6, 1, "Family feud", 0),
    (7, 1, "Moving", 0),
    (8, 2, "Room/bed", 1),
    (9, 2, "School", 0), 
    (10, 2, "Internet", 0),
    (11, 2, "Mall", 0),
    (12, 2, "Friend's house", 0), 
    (13, 2, "Park", 0),
    (14, 2, "Work", 0),
    (15, 3, "Church", 0),
    (16, 3, "Groceries/shopping", 1), 
    (17, 3, "Laundry", 0),
    (18, 3, "Clean the house", 0),
    (19, 3, "Sleep in", 0), 
    (20, 3, "Eat out", 0);
    """

    pop_score = """
    INSERT INTO score VALUES
    (1, 1, 29),
    (2, 2, 22), 
    (3, 3, 18),
    (4, 4, 12),
    (5, 5, 10), 
    (6, 6, 5),
    (7, 7, 2),
    (8, 8, 28),
    (9, 9, 22), 
    (10, 10, 16),
    (11, 11, 12),
    (12, 12, 10), 
    (13, 13, 4),
    (14, 14, 4),
    (15, 15, 35),
    (16, 16, 24), 
    (17, 17, 12),
    (18, 18, 6),
    (19, 19, 6), 
    (20, 20, 4);
    """

    pw = input("Please enter password to access FamilyFeud Database: ")
    db = str(input("Please specify database you'd like to connect to: "))

    connection = create_db_connection("localhost", "odos", pw, db)
    execute_query(connection, pop_questionnare)
    execute_query(connection, pop_answers)
    execute_query(connection, pop_score)


def intiate_database():
    
    password = input("Please enter password to access FamilyFeud Database: ")
    database_name = str(input("Please specify how you'd like the database to called: "))

    connection = create_server_connection("127.0.0.1", "odos", password)
    query = "CREATE DATABASE " + database_name

    create_database(connection, query)
    create_tables()
    fill_initial_data()
    



create_tables()


