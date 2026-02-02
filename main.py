import os
import time
from pygame import mixer

mixer.init()
mixer.music.load("Pymodoro/erro.mp3")

focusTime = 25 * 60
shortRest = 5 * 60
longRest = 15 * 60

for i in range(focusTime,-1,-1):
    os.system('clear')
    min,sec = divmod(i,60)
    print(f"{min:02}:{sec:02}")
    time.sleep(1)
mixer.music.play()

for i in range(shortRest,-1,-1):
    os.system('clear')
    min,sec = divmod(i,60)
    print(f"{min:02}:{sec:02}")
    time.sleep(1)
mixer.music.play()

for i in range(focusTime,-1,-1):
    os.system('clear')
    min,sec = divmod(i,60)
    print(f"{min:02}:{sec:02}")
    time.sleep(1)
mixer.music.play()

for i in range(shortRest,-1,-1):
    os.system('clear')
    min,sec = divmod(i,60)
    print(f"{min:02}:{sec:02}")
    time.sleep(1)
mixer.music.play()

for i in range(focusTime,-1,-1):
    os.system('clear')
    min,sec = divmod(i,60)
    print(f"{min:02}:{sec:02}")
    time.sleep(1)
mixer.music.play()

for i in range(longRest,-1,-1):
    os.system('clear')
    min,sec = divmod(i,60)
    print(f"{min:02}:{sec:02}")
    time.sleep(1)
mixer.music.play()