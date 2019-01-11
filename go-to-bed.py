import time
import datetime
import os

late_time_h = 23
late_time_m = 30

early_time_h = 4
early_time_m = 0

is_night = False

print("Starting, late time is " + str(late_time_h) + ":" + str(late_time_m))

while True:

    if is_night:
        print("Shutting down!")
        os.system("shutdown")
        break
    else:
        now = datetime.datetime.now()
        print("Current time is: " + str(now.hour) + ":" + str(now.minute))

        if (now.hour > late_time_h or (now.hour == late_time_h and now.minute > late_time_m)) or (now.hour < early_time_h or(now.hour == early_time_h and now.minute < early_time_m)):
            print("It is now night")
            is_night = True
        else:
            time.sleep(10)
