import time
from datetime import datetime
import winsound

alarm_time = input("Enter time for alarm :")
print("Alarm set for:",alarm_time)

while True:
    current_time=datetime.now().strftime("%H:%M:%S")

    if(current_time == alarm_time):
        print("Wake up! Alarm ringing")
        for i in range(10):
            winsound.Beep(1000,5000)
            time.sleep(1)
        break
    time.sleep(1)