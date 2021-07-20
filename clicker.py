import time
import pyautogui # neccecary library for keyboard/mouse integration in Python3.xx

pyautogui.FAILSAFE = True # neccecary to exit the program.

def main():
    start = input(str("Start autoclicker? y/N? "))
    if start == "y":
        print("sleeping for 10 seconds")
        time.sleep(10)
        while True:
            pyautogui.moveTo(1143,373) # pixels of the "flirt" button, screen resolution 1920*1080
            pyautogui.doubleClick(1143,373) # double clicks the "flirt" button.
    else:
        return 1 # standard C output for IO error.
        exit()
    
main() # run main function.    
