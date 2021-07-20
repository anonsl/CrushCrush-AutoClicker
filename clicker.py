import time
import pyautogui


pyautogui.FAILSAFE = True

def main():
    start = input(str("Start autoclicker? y/N? "))
    if start == "y":
        print("sleeping for 10 seconds")
        time.sleep(10)
        print(time.asctime)
        while True:
            for i in range(0,1):
                pyautogui.moveTo(1143,373)
                pyautogui.doubleClick(1143,373)
                pyautogui.doubleClick(1143,373)
main()