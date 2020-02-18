import sqlite3
from datetime import datetime
from os import path

def create_table_count():
	if path.isfile('./db/list.db') == False:
		conn = sqlite3.connect('./db/list.db')
		c = conn.cursor()
		c.execute("CREATE TABLE all_base (name_db, current_date)")
		conn.commit()
		conn.close()


create_table_count()

def get_table_count(string):
	conn = sqlite3.connect('./db/list.db')
	c = conn.cursor()
	
	if string == 'id':
		result = [i for i in c.execute('''SELECT rowid FROM all_base 
										ORDER BY rowid DESC LIMIT 1''')]
	else:
		result = [i for i in c.execute('''SELECT name_db FROM all_base 
											ORDER BY rowid DESC LIMIT 1''')]
											
	conn.commit()
	conn.close()
	return result[0][0]
	
#print(get_table_count('name'))
	
	
	
def set_table_count(db_name):
	conn = sqlite3.connect('./db/list.db')
	c = conn.cursor()
	date = datetime.now()
	c.execute("INSERT INTO all_base VALUES (?, ?)", (db_name, date))	
	conn.commit()
	conn.close()
	return db_name
	


def check_string(string):
	break_create = ['=','""',"''", '-','+', '(', ')',]
	check_list = [i for i in string for j in break_create if i == j]
	if check_list == []:
		return string
	else:
		raise ValueError('Access dennied')



def check_kwargs(**kwargs):
	columns_list = [key+ ' ' + value for key, value in kwargs.items()]
	return check_string(', '.join(columns_list))

#print(check_kwargs(quote='text', author='text', comments='real'))
		
		
		
def create(db_name, **kwargs):
	create_table_count()
	name = set_table_count(db_name) + '_' + str(get_table_count('id'))
	conn = sqlite3.connect('./db/'+ name +'.db')
	c = conn.cursor()
	c.execute(f'''CREATE TABLE {check_string(set_table_count(db_name))}
								({check_kwargs(**kwargs)})''')
	conn.commit()
	conn.close()
	names = [name, db_name]
	return names



def insert(db_name, data_set):
	conn = sqlite3.connect('./db/' + db_name[0] + '.db')
	c = conn.cursor()
	c.executemany(f"INSERT INTO {db_name[1]} VALUES (?, ?)", (data_set))
	conn.commit()
	conn.close()
	


