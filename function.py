from pygame import mixer
import pyfiglet
from pathlib import Path
import json
import os
import time as tm

import JSONconfig 

def play_sound():
    ROOT_FILE = Path(__file__).parent
    SOUNDFILE_PATH = ROOT_FILE / "erro.mp3"

    mixer.init()

    mixer.music.load(SOUNDFILE_PATH)
    mixer.music.play()


def chronoTimer():

    with open(JSONconfig.JSON_FILE,"r") as arquivo:
        data = json.load(arquivo)

    for i in data["Sequence"]:
        os.system('clear')
        time = data[i] * 60

        while time >= 0:
            os.system('clear')
            min,sec = divmod(time,60)
            print(pyfiglet.figlet_format(f"{min:02} : {sec:02}", font= "computer"))
            tm.sleep(1)
            time -= 1
        
        play_sound()

        option = input("Do you want to continue ? (Y/n)")
        if option == "Y" or "y":
            pass
        else:
            break

chronoTimer()