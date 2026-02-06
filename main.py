import os
import time
from pygame import mixer
import pyfiglet

## Essa sequencia de funçoes é só para fazer o codigo ficar mais simple(para mim)
def time2focus():
    focusTime = 25 * 60
    
    for i in range(focusTime,-1,-1):
        os.system('clear')
        min,sec = divmod(i,60)
        print(pyfiglet.figlet_format(f"{min:02} : {sec:02}", font= "computer"))
        time.sleep(1)

    mixer.music.play()

def time2shortrest():
    shortRest = 5 * 60
    for i in range(shortRest,-1,-1):
        os.system('clear')
        min,sec = divmod(i,60)
        print(pyfiglet.figlet_format(f"{min:02} : {sec:02}", font= "computer"))
        time.sleep(1)

    mixer.music.play()

def time2longrest():
    longRest = 15 * 60

    for i in range(longRest,-1,-1):
        os.system('clear')
        min,sec = divmod(i,60)
        print(pyfiglet.figlet_format(f"{min:02} : {sec:02}", font= "computer"))
        time.sleep(1)

    mixer.music.play()


mixer.init()
mixer.music.load("Pymodoro/erro.mp3")

time2focus()

os.system("clear")
continueOption = input("Continuar?\n")
if continueOption == "S": time2shortrest() 
else:
    os.system('clear')

os.system("clear")
continueOption = input("Continuar?\n")
if continueOption == "S": time2focus() 
else:
    os.system('clear')

os.system("clear")
continueOption = input("Continuar?\n")
if continueOption == "S": time2shortrest() 
else:
    os.system('clear')

os.system("clear")
continueOption = input("Continuar?\n")
if continueOption == "S": time2focus() 
else:
    os.system('clear')

os.system("clear")
continueOption = input("Continuar?\n")
if continueOption == "S": time2longrest() 
else:
    os.system('clear')
