import pytz
import datetime


moscow = 'Europe/Moscow'
tz_moscow = pytz.timezone(moscow)
moscow_time = datetime.datetime.now(tz=tz_moscow)


kiev = 'Europe/Kiev'
tz_kiev = pytz.timezone(kiev)
kiev_time = datetime.datetime.now(tz=tz_kiev)

print(moscow_time)
print(kiev_time)

#for tz in pytz.all_timezones:
count = 0
for tz in pytz.country_timezones:
	print(f'''{tz}\t {pytz.country_names[tz]}
\t {pytz.country_timezones[tz][0]}
''')
	count += 1
	if count == 7:
		break
		

		
while True:
	tz = input('TZ: ').upper()
	if tz == 'Q':
		break
	else:	
		for i in pytz.country_timezones:
			if tz == i:
				print(f'''{i}\t {pytz.country_names[i]}
\t {pytz.country_timezones[i][0]}

{datetime.datetime.now(tz=pytz.timezone(pytz.country_timezones[i][0]))}
''')



#print(datetime.datetime.today())
#print(datetime.datetime.now())
