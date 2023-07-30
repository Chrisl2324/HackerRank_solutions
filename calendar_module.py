import calendar

date = list(map(int, input().split()))
day_of_week = calendar.weekday(date[2], date[0], date[1])
day_of_week_name = calendar.day_name[day_of_week]
print(day_of_week_name.upper())




