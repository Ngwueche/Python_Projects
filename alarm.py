import datetime
from playsound import playsound

alarmHr = int(input("Enter the Hour: "))
alarmMin = int(input("Enter the Min: "))
alarm_AM_PM = input("AM / PM: ")

if alarm_AM_PM == "PM":
    alarmHr+=12

while True:
    if alarmHr == datetime.datetime.now().hour and alarmMin == datetime.datetime.now().minute:
        print("playing...")
        playsound("C:/Users/THIS PC/Music/2Baba-Smile.mp3")
        break
