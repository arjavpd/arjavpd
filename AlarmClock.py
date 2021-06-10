from datetime import datetime
import time

counter = 0
while counter == 0:
    alarm_hour = int(input("Enter hour (24 hour)\n"))
    alarm_minute = int(input("Enter minute\n"))
    print("You choose {}:{}.".format(alarm_hour, alarm_minute))
    print("Is this correct? (Y/N)")
    confirmation = input()
    if confirmation == 'Y':
        counter = 1


now = datetime.now()

current_hour = abs(int(now.strftime("%H")))
hours_left = alarm_hour-current_hour

current_minute = abs(int(now.strftime("%M")))
minutes_left = alarm_minute-current_minute
seconds_left = (hours_left*60*60)+(minutes_left*60)
time.sleep(seconds_left)
print("WAKE UPPPP!!")

