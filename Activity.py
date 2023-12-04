import time
from playsound import playsound
userInput = int(input("What is the time in seconds?"))

def count_down_timer(t1):
    while t1>0:
        minutes = int(t1/60)
        seconds = int(t1%60)
        if t1>=10:
            print(minutes, ":" , seconds)
        elif t1<10:
            print(str(minutes)+ " : 0"+ str(seconds))
        time.sleep(1)
        t1 -= 1
    playsound("mixkit-sound.wav")
    print("Times UP")
    


count_down_timer(userInput)

