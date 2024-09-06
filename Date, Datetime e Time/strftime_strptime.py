import datetime

d = datetime.datetime.now()

print(d.strftime("%d/%m/%Y %H:%M"))

date_string = "06/09/2024 12:06"
d = datetime.datetime.strptime(date_string,"%d/%m/%Y %H:%M")
print(d)