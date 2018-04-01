# A Pomodoro timer is a well-known productivity interval that has been shown to improve your productivity.
# It gives you a prescribed interval of 25 minutes of work followed by a 5-minute break.
# After 4 work intervals, there is a 15-minute break.
from datetime import datetime
from datetime import timedelta
import winsound


def play_sound():
    winsound.PlaySound('sound.wav', winsound.SND_FILENAME)


def count_time(wi, output, interval_number):
    cnt = 0
    while cnt > -1:
        if datetime.now() > wi:
            cnt = -1
            play_sound()
            interval_number += 1
            if interval_number == 10:
                print('Pomodoro Finished')
                return -1
            if interval_number % 2 == 0:
                print(msg[1])
            else:
                if interval_number == 9:
                    print(msg[2])
                else:
                    print(msg[0])
    return interval_number

st = datetime.now()

msg = ['Congrats, you have finished a productivity period. Take a short break.',
       'Back to it! Breaks over.',
       'Congrats, you have finished a productivity period. Take a long break.']


print('Start Working')

# Work Unit
lwu = 10
# Short Break
sb = 1
# Long break
lb = 5

for i in range(0, 10):
    if i % 2 == 0:
        r = lwu
    else:
        if i == 9:
            r = lb
        else:
            r = sb
    i = count_time(datetime.now() + timedelta(minutes=r), msg, i)


