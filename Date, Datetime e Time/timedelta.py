import datetime

d = datetime.datetime(2024, 9, 6, 11, 48)
print(d)

# adicioanndo mais duas semanas
d = d + datetime.timedelta(weeks=2)
print(d)