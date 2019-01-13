from datetime import datetime

str_today = datetime.now()

print(datetime.today().strftime("%Y/%m/%d %H:%M:%S"))

str_today = datetime.now()
print(str_today.year, str_today.month, str_today.day)
print(type(str_today))