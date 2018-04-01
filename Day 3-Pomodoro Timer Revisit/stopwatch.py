from datetime import datetime
from datetime import timedelta
import winsound


def play_sound():
    winsound.PlaySound('sound.wav', winsound.SND_FILENAME)

print('Welcome to #100DaysOfPython, here is a stopwatch/timer app')

print('Would you like to set a timer [0] or a stopwatch [2]?')
print('0 = timer')
print('1 = stopwatch')

choice = input("Enter your choice\n")

if int(choice) == 0:
    min = input("Enter the amount of minutes you would like to set your timer\n")
    if int(min) > 0 <= 1440:
        dt = datetime.now()
        at = dt + timedelta(minutes=int(min))
        cnt = 1
        while cnt > -1:
            if datetime.now() > at:
                cnt = -1
                play_sound()
                print('timer done!\n{0}\n{1}'.format(dt, at))
elif int(choice) == 1:
    input('Simple stopwatch without laps. Hit enter to start counting.')
    start = datetime.now()
    input('Hit enter to stop counting.')
    end = datetime.now()
    print('Elapsed time: {0}'.format(end - start))
else:
    print("Sorry, I couldn't quite catch that. Try again.")



