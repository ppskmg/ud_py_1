import sqlite3
from os import path

def create_table_questions():
	if path.isfile('./db/questions.db') == False:
		conn = sqlite3.connect('./db/questions.db')
		c = conn.cursor()
		c.execute("CREATE TABLE questions (test_id, question, correct_answer, average_correct)")
		conn.commit()
		conn.close()


create_table_questions()
