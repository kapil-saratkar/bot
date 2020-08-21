import os
import pyttsx3
from pyfiglet import Figlet
custom_fig = Figlet(font='big')
print(custom_fig.renderText('OMEN'))
from tqdm import tqdm
loop = tqdm(total=2000,position=0,leave=True)
for k in range(0,2000):
    loop.set_description("Initalizing OMEN...".format(k))
    loop.update(1)
loop.close()
pyttsx3.speak(" Hello I am OMEN your personal assistant")
print("Hello I am OMEN your personal assistant")
print("suggestion : If you are new to use OMEN try 'what can you do for me' ")
while True:
    print("OMEN- How can I help you sir :"  , end='')
    p = input()
    if(("what can you do for me" in p) or ("launch any" in p)):
        pyttsx3.speak(" I am designed to launch applications for user  you can launch any application from the  list below ")
        print("OMEN- I can launch any application from the list")
        print(" |+ GoogleChrome  +| ")
        print(" |+ MicrosoftEdge +|")
        print(" |+ Notepad       +| ")
        print(" |+ VLCmediaPlayer+| ")
        print("suggestion : Use run or execute to launch the application")
    elif ("run" in p)  and ("chrome" in p):
        loop = tqdm(total=1000,position=0,leave=False)
        for k in range(0,1000):
            loop.set_description("Launching Chrome Browser".format(k))
            loop.update(1)
        loop.close()
        print(">> application launched ")
        os.system("chrome")      
    elif ("run" in p)  and ("MicrosoftEdge" in p):
        loop = tqdm(total=1000,position=0,leave=False)
        for k in range(0,1000):
            loop.set_description("Launching Microsoft Browser".format(k))
            loop.update(1)
        loop.close()
        print(">> application launched ") 
        os.system("chrome")
           
    elif (("run" in p) or  ("execute" in p )) and  (("notepad" in p) or ("editor" in p) ) :
        
        loop = tqdm(total=1000,position=0,leave=False)  
        for k in range(0,1000):
            loop.set_description("Launching Notepad".format(k))
            loop.update(1)
        loop.close()
        print(">> application launched ")
        os.system("notepad")
        
    elif ("run" in p)  and ("player" in p) and ("media" in p):
        loop = tqdm(total=1000,position=0,leave=False)
        for k in range(0,1000):
            loop.set_description("Launching VLCMediaPlayer".format(k))
            loop.update(1)
        loop.close()
        print(">> application launched ")
        os.system("vlc")
        
    elif  ("exit" in p)  or ("quit" in p):
        loop = tqdm(total=1400,position=0,leave=False)
        for k in range(0,1400):
            loop.set_description("Shutting Down OMEN".format(k))
            loop.update(1)
        pyttsx3.speak(" Shutting Down OMEN")   
        loop.close()
        break
    else:
        pyttsx3.speak(" Invalid command found ")
        print("Invalid command found")


