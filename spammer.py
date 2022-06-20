import pyautogui
import time
import random

print("""
  _____
 / ____|
| (___  _ __   __ _ _ __ ___  _ __ ___   ___ _ __
 \___ \| '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
 ____) | |_) | (_| | | | | | | | | | | |  __/ |
|_____/| .__/ \__,_|_| |_| |_|_| |_| |_|\___|_|
       | |                                        """)

word = input("What Message?: ")
x = int(input("How many Times? : "))
delay = int(input("Any Delay? : "))

y = 0

sent = 0

time.sleep(7)

for i in range(y,x):
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    sent = sent + 1
    print("Sent %s Messages!"%(sent))
    time.sleep(delay)
