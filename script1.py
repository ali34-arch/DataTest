import time
from datetime import datetime, timedelta
def timer_system(start):
    while start!=0:
        start -= 1
        time.sleep(1)
        print(start)
x = datetime.today()
def timer_numbers():
    hours = int(input("Enter Hours: "))
    hours = abs(-hours) #turns negatives into positives
    minutes = int(input("Enter Minutes: "))
    minutes = abs(-minutes)
    seconds = int(input("Enter Seconds: "))
    seconds = abs(-seconds)
    update_time = x + timedelta(hours=hours, minutes=minutes)
    print(f"Timer Completes: {update_time}")
    start = (hours * 3600) + (minutes * 60) + seconds
    timer_system(start)
timer_numbers()

print("Timer Completed")
