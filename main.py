import os
import time
from pathlib import Path
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

## Caminho do arquivo .mp3
### Agora nem você ou eu vamos ter que copiar o caminho do arquivo .mp3 para que o codigo funcione kk
ROOT_FILE = Path(__file__).parent
SOUNDFILE_PATH = ROOT_FILE / "erro.mp3"

mixer.music.load(SOUNDFILE_PATH)
mixer.music.play()

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
