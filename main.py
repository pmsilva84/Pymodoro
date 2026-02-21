import function as pom
import os
import pyfiglet

os.system("clear")
print(pyfiglet.figlet_format("Pymodoro", font= "computer")) ## A bendiata do menu iniciar 
print("Made by P.A." + ("\n"*2))

try :
    #
    start = input("Start? (Y/n)")
    if start == "Y" or "y": 
        pom.chronoTimer()
        
    elif start == "N" or "n": 
        os.system("clear")
        print("bye bye...")

except KeyboardInterrupt:
    os.system("clear")
    print("Error")