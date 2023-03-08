import datetime

day = input("What is your birthday? ")
print(day)
birth = datetime.datetime.strptime(day, '%Y/%m/%d')
print(birth.date())
Date = datetime.date.today()
print(birth.date() - Date)
