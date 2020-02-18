from datetime import date

year = int(input('Year: '))
month = int(input('Month: '))
day = int(input('Day: '))

days = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']
week_day = date(year, month, day).weekday()

print('Day: ' + days[week_day])
