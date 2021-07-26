import time
import pyautogui


pyautogui.FAILSAFE = True

def main():
    runFlirt = input(str(r"Options: 1) Flirt autoclicker 2) Date autoclicker(use: set the chosen date you need and start the script) 3) exit.")).lower()
    print("Default startup duration 10 seconds.")
    if runFlirt == "1":
        time.sleep(10)
        return flirtClick()
    elif runFlirt == "2":
        time.sleep(10)
        return dateClick()
    else:
        exit()    

    
def flirtClick():
    while True:
        pyautogui.moveTo(1143,373)
        pyautogui.doubleClick(1143,373, 0.0001)
            

def dateClick():
    while True:
        pyautogui.moveTo(573, 790)
        pyautogui.doubleClick(573, 790)




main()
