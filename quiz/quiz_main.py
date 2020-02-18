import sqlite3


def create_table_answer():
	if path.isfile('./db/answers.db') == False:
		conn = sqlite3.connect('./db/answers.db')
		c = conn.cursor()
		c.execute("CREATE TABLE answers (test_id, user_name, correct, time_spent, score, best_score )")
		conn.commit()
		conn.close()

questions = []

for q in questions:
	print(q)
	answer = input('Input answer:').lower()
	if answer == questions.answer:
		print('Correct')




