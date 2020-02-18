import sqlite3

db_name = 'data_set_3'
conn = sqlite3.connect('./db/' + db_name + '.db')
c = conn.cursor()
select = c.execute("SELECT magnitude, place FROM data_set ORDER BY magnitude ASC" )

for i in select:
	print(i[0], i[1])
print(len()
conn.commit()
conn.close()
