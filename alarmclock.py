import datetime
import time
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def alarm_clock():
    clear_console()
    print("==== Simple Python Alarm Clock ====")
    alarm_time = input("Set alarm time (HH:MM AM/PM): ").strip()

    try:
        # Convert input to 24-hour format datetime
        alarm_hour = int(alarm_time.split(":")[0])
        alarm_minute = int(alarm_time.split(":")[1][:2])
        am_pm = alarm_time[-2:].upper()

        if am_pm == "PM" and alarm_hour != 12:
            alarm_hour += 12
        elif am_pm == "AM" and alarm_hour == 12:
            alarm_hour = 0

    except Exception as e:
        print("Invalid time format. Please use HH:MM AM/PM format.")
        return

    print(f"Alarm is set for {alarm_time}...\n")

    while True:
        now = datetime.datetime.now()
        current_hour = now.hour
        current_minute = now.minute
        current_second = now.second

        if current_hour == alarm_hour and current_minute == alarm_minute:
            print("⏰ WAKE UP! ALARM TIME! ⏰")
            try:
                for _ in range(5):
                    print('\a')  # Beep sound
                    time.sleep(1)
            except:
                print("Alarm ringing!")
            break

        time.sleep(1)

if __name__ == "__main__":
    alarm_clock()
