from tkinter import *
import datetime
import time
import winsound
from threading import Thread

root = Tk()
root.geometry("400x250")

def Threading():
    t1 = Thread(target=alarm)
    t1.start()

def alarm():
    while True:
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        current_time_label.config(text="Current Time: " + current_time)

        if current_time == set_alarm_time:
            alarm_status.config(text="Time to Wake up!")
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
            break

        time.sleep(1)

Label(root, text="Alarm Clock", font=("Helvetica 20 bold"), fg="red").pack(pady=10)
Label(root, text="Set Time", font=("Helvetica 15 bold")).pack()

frame = Frame(root)
frame.pack()

hour = StringVar(root)
hours = [str(i).zfill(2) for i in range(24)]
hour.set(hours[0])

hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

minute = StringVar(root)
minutes = [str(i).zfill(2) for i in range(60)]
minute.set(minutes[0])

mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

second = StringVar(root)
seconds = [str(i).zfill(2) for i in range(60)]
second.set(seconds[0])

secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)

Button(root, text="Set Alarm", font=("Helvetica 15"), command=Threading).pack(pady=20)

current_time_label = Label(root, text="Current Time: ", font=("Helvetica 12"))
current_time_label.pack()

alarm_status = Label(root, text="", font=("Helvetica 15"))
alarm_status.pack()

root.mainloop()
