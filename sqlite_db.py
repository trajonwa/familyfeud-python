import sqlite3
import random
from classes import GameCard



db_name = "familyfeud_db"

def create_tables():

    with sqlite3.connect(db_name) as conn:

        cursor_obj = conn.cursor()

        cursor_obj.execute("""
                        CREATE TABLE questionnare (
                        question TEXT PRIMARY KEY,
                        question_id INTEGER
                        )
                        """
                        )

        cursor_obj.execute("""
                        CREATE TABLE answers (
                        answer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        question_id INTEGER NOT NULL,
                        answer TEXT NOT NULL,
                        multiple_answers INTEGER NOT NULL,
                        FOREIGN KEY(question_id) REFERENCES questionnare(question_id) ON DELETE CASCADE)
                        """
                        )

        cursor_obj.execute("""
                        CREATE TABLE scores (
                        score_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        answer_id INTEGER NOT NULL,
                        score INTEGER NOT NULL,
                        FOREIGN KEY(answer_id) REFERENCES answers(answer_id) ON DELETE CASCADE )
                        """
                        )


def intial_data():

    with sqlite3.connect(db_name) as conn:
        cursor_obj = conn.cursor()

        cursor_obj.execute("""INSERT INTO questionnare (question_id, question) VALUES
                                (1, "Name a reason you might get rid of an old family heirloom."),
                                (2, "Where do kids nowadays spend most of their time?"), 
                                (3, "Tell me something many people do just once a week.")
                                                        """)

        cursor_obj.execute("""INSERT INTO answers (answer_id, question_id, answer, multiple_answers) VALUES
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
                                (20, 3, "Eat out", 0)
                                """)

        cursor_obj.execute("""INSERT INTO scores (score_id, answer_id, score) VALUES
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
                                (20, 20, 4)
                                """)


def fetch_all():

    with sqlite3.connect(db_name) as conn:

        cursor_obj = conn.cursor()
        cursor_obj.execute("""
                            SELECT question, answer, score, multiple_answers FROM 
                            questionnare q JOIN answers a ON q.question_id = a.question_id
                            JOIN scores s ON a.answer_id = s.answer_id;
                            """)

        data = cursor_obj.fetchall()
        print(data)
        current_question = data[0][0]
        card = GameCard(current_question)

        for row in data:
            if row[0] == current_question:

                if row[3] == 0:

                    card.answers[row[1].upper()] = (row[2], {})
                else:

                    temp_list = row[1].split("/")
                    for ans in range(len(temp_list)):
                        temp_list[ans] = temp_list[ans].upper()
                    card.answers[row[1].split("/")[0].upper()] = (row[2], set(temp_list))

            else:

                current_question = row[0]
                card = GameCard(current_question)

                if row[3] == 0:
                    card.answers[row[1].upper()] = (row[2], {})

                else:

                    temp_list = row[1].split("/")
                    for ans in range(len(temp_list)):
                        temp_list[ans] = temp_list[ans].upper()
                    card.answers[row[1].split("/")[0].upper()] = (row[2], set(temp_list))


def add_card_to_db(question, list_of_answers):

    with sqlite3.connect(db_name) as conn:
    
        cursor_obj = conn.cursor()
        random_key1 = random.randint(12, 99999999)
        random_key2 = random.randint(12, 99999999)
        random_key3 = random.randint(12, 99999999)
        count_to_make_unique = 0

        cursor_obj.execute("""INSERT INTO questionnare (question_id, question) VALUES
                            (?, ?)
                            """, (random_key1, question))

        for ans_list in list_of_answers:

            all_answers = ans_list[0].split("/")

            print(ans_list[0])
            if len(all_answers) > 1:

                cursor_obj.execute("""INSERT INTO answers (answer_id, question_id, answer, multiple_answers) VALUES
                                    (?, ?, ?, ?)""", (random_key2 + count_to_make_unique, random_key1, ans_list[0], 1))

            else:

                cursor_obj.execute("""INSERT INTO answers (answer_id, question_id, answer, multiple_answers) VALUES
                                    (?, ?, ?, ?)""", (random_key2 + count_to_make_unique, random_key1, ans_list[0], 0))

            cursor_obj.execute("""INSERT INTO scores (score_id, answer_id, score) VALUES
                                    (?, ?, ?)""", (random_key3 + count_to_make_unique, random_key2 + count_to_make_unique,\
                                                ans_list[1]))

            count_to_make_unique += 1
