import sqlite3
from os import path
import time

def create_table_tests():
	if path.isfile('./db/tests.db') == False:
		conn = sqlite3.connect('./db/tests.db')
		c = conn.cursor()
		c.execute("CREATE TABLE tests (test_name, number_questions, score)")
		conn.commit()
		conn.close()

	
	
def insert_test(test_name):
	conn = sqlite3.connect('./db/tests.db')
	c = conn.cursor()	
	c.execute("INSERT INTO tests VALUES (?, ?, ?)", (test_name, 0, 0))
	conn.commit()
	conn.close()	
		
		
				
def create_table_questions():
	if path.isfile('./db/questions.db') == False:
		conn = sqlite3.connect('./db/questions.db')
		c = conn.cursor()
		c.execute("CREATE TABLE questions (test_id, question, correct_answer, average_correct)")
		conn.commit()
		conn.close()
		
		
		
def insert_question(test_id, question, correct_answer):
	conn = sqlite3.connect('./db/questions.db')
	c = conn.cursor()	
	c.execute("INSERT INTO questions VALUES (?, ?, ?, ?)", (test_id, question, correct_answer, 0))
	conn.commit()
	conn.close()



def get_questions():			
	conn = sqlite3.connect('./db/questions.db')	
	c = conn.cursor()
	questions = c.execute("SELECT question, correct_answer FROM questions")
	questions_list = []
	for i in questions:
		questions_list.append(i)
	conn.commit()
	conn.close()
	return questions_list



def create_table_answers():
	if path.isfile('./db/answers.db') == False:
		conn = sqlite3.connect('./db/answers.db')
		c = conn.cursor()
		c.execute("CREATE TABLE answers (test_id, user_name, correct, time_spent, score real)")
		conn.commit()
		conn.close()
		
		
		
def insert_answer(test_id, user_name, correct, time_spent, score):
	conn = sqlite3.connect('./db/answers.db')
	c = conn.cursor()	
	c.execute("INSERT INTO answers VALUES (?, ?, ?, ?, ?)", (test_id, user_name, correct, time_spent, score))
	conn.commit()
	conn.close()



def get_best_score(user_name, test_id):
	conn = sqlite3.connect('./db/answers.db')	
	c = conn.cursor()
	best_score = c.execute("SELECT score FROM answers WHERE user_name=:name and test_id=:id ORDER BY score DESC LIMIT 1", {'name':user_name, 'id':test_id})
	b_score = []
	for i in best_score:
		b_score.append(i)
	conn.commit()
	conn.close()
	return b_score



def get_tests():			
	conn = sqlite3.connect('./db/tests.db')	
	c = conn.cursor()
	tests = c.execute("SELECT rowid, test_name FROM tests")
	tests_list = []
	for i in tests:
		tests_list.append(i)
	conn.commit()
	conn.close()
	return tests_list
	
	

def input_question(test_id):
	question = input('Input question: ')
	correct_answer = input('Input correct answer: ')
	insert_question(test_id, question, correct_answer)
	print('Test add: ', test_id, question, correct_answer)
	
	

create_table_tests()
create_table_questions()
create_table_answers()

		
print('''


	Command for app
	
	new test: T
	new question: Q
	show all tests: SHOW TESTS
	testing: TESTING
	''')
				
while True:
	new = input('Command: ').lower()
	
	if new == 't':
		while True:
			test_name = input('Input name for test: ')
			if test_name != '':
				insert_test(test_name)
			if input('Add another test Y/N: ').lower() != 'y':
				break
				
	elif new == 'q':
		test_id = input('Input test id: ')
		while True:
			input_question(test_id)
			if input('Add another question Y/N: ').lower() == 'n':
				break
				
	elif new =='show tests':
		tests = get_tests()
		for i in tests:
			print('ID ' + str(i[0]) + ': ', i[1])
		
	elif new == 'testing':
		
		tests = get_tests()
		for i in tests:
			print('ID ' + str(i[0]) + ': ', i[1])
		
		correct = 0
		time_spent = 0
		test_id = input('\n \n Input test ID: ')
		user_name = input('\n \n Your login: ')
		questions = get_questions()
		
		for q in questions:
			print('\n\nQuestion: ' + q[0])
				
			time_start = time.perf_counter()	
			answer = input('y/n: ').lower()

			if answer == q[1]:
				correct += 1
				print('Correct \n')
			else:
				print('Wrong \n')
				
			end_time = time.perf_counter()
			time_spent += end_time - time_start
		
		score = 100 / ( len(questions) / correct )
		
		
		best_score = get_best_score(user_name, test_id)
		insert_answer(test_id, user_name, correct, time_spent, score)
		

		
		
		
		print(f'''		
		Time left: {format(time_spent, '.2f')}
		Correct answer: {correct} of {len(questions)}
		You score: {score}
		Best score: {best_score[0][0]}
		''')
