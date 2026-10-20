import datetime

print("-" * 30, "Exercice", "-" * 30)

now = datetime.datetime.now()

print(f"1.\t Current date : {now}")

formatted_date = now.strftime("%m%d%Y, %H:%M:%S")

print(f"2.\t Current time formatted : {formatted_date}")

date_string = "5 December, 2019"

parsed_date = datetime.datetime.strptime(
    date_string, "%d %B, %Y"
)

print(f"3.\t Date from string : {parsed_date}")

current_date = datetime.date(2026, 10, 10)
new_year = datetime.date(2027, 1, 1)

print(f"4.\t Time left before new year : {new_year - current_date}")

print(f"5.\t Time from 1970 and now : {now.timestamp()}")

print("6.\t I can use datetime module to normalize dates by months in my project Job Market Intelligence")