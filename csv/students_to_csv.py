import csv


def write_student(name, last_name, age):
	
	header = ['name', 'last_name', 'age']
	
	try:
		with open('students.csv', 'x') as file:
			writer = csv.DictWriter(file, fieldnames=header, delimiter='|')
			writer.writeheader()
			writer.writerow({'name':name, 'last_name':last_name, 'age':age})
	except FileExistsError:
		with open('students.csv', 'a') as file:
			writer = csv.DictWriter(file, fieldnames=header, delimiter='|')
			writer.writerow({'name':name, 'last_name':last_name, 'age':age})
		
		
	write_student('Juli', 'Marko', 34)
