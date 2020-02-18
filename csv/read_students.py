import csv


def read_students():
	with open('students.csv') as file:
		read = csv.DictReader(file, delimiter='|')
		for row in read:
			print(f'''
			First name: {row["name"]}
			Last name:  {row["last_name"]} 
			Age:        {row["age"]}
			
			''')
			

read_students()
