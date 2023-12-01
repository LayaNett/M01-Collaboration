"""Layla Nettavong
Python M06 programming assignment
13.1-3
"""
import datetime

#13.1
Date = datetime.date.today()

with open("today.txt","w") as f:
    f.write(str(Date))

#13.2
f = open("today.txt")
today_string = f.read()
print(today_string)
f.close()

#13.3
today_string = today_string.split("-")
print(today_string)