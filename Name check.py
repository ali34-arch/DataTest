import time
from datetime import datetime
global year
year = datetime.now().year


def space_check(Date):
    return Date.strip() != ""
def length_check(Date):
    return len(Date) == 4
def response(date, year):
   if year - date >= 25:
       print("Old\n")
   elif year - date <= 10:
       print("Fetus\n")
def negative_check(date):
    return date > 0


while True:
    try:
        time.sleep(1)
        date = int(input("Enter your Birth Year: "))
        Date = str(date)
        if not space_check(Date):
            print("Invalid Date\n")
        elif not length_check(Date):
            print("Invalid Date\n")
        elif not negative_check(date):
            print("Invalid Date\n")
        else:
            response(date, year)
            break
    except ValueError:
        print("Invalid Date\n")

print("Date accepted")
