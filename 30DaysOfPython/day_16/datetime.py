import datetime

print("-"*30,"Exercice","-"*30)

now = datetime.now()


print(f"1.\t Current date : {now}")

now = now.strftime("%m%d%Y, %H:%M:%S")

print(f"2.\t Current time formatted : {now}")

date = "5 December, 2019"

date = datetime.strptime(date,"%d %B, %Y")

print(f"3.\t Date from string : {date}")

now = datetime.date(year=2026,month=10,day=10)
new_year = datetime.date(year=2027,month=1,day=1)

print(f"4.\t Time left before new year : {new_year - now}")

now = datetime.now()

print(f"5.\t Time from 1970 and now : {now.timestamp()}")

print("6.\t I can use datetime module to normalize dates by months in my project JobMarket Intelligence")