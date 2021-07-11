import time
import pyautogui as pt
import random
import webbrowser

print("""
  _____
 / ____|
| (___  _ __   __ _ _ __ ___  _ __ ___   ___ _ __
 \___ \| '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
 ____) | |_) | (_| | | | | | | | | | | |  __/ |
|_____/| .__/ \__,_|_| |_| |_|_| |_| |_|\___|_|
       | |                                        """)

link = input("Link: ")
word = input("What Message?: ")
k = int(input("How many Times? : "))
delay = 1

z = 0

sent = 0

webbrowser.open(link)
time.sleep(7)
#X:  879 Y:  525
pt.click(880,525)
time.sleep(2)
position1 = pt.locateOnScreen("at.png", confidence=.7)
x = position1[0]
y = position1[1]

pt.moveTo(x,y, duration=.05)
pt.moveTo(x - 170, y + 22, duration = .5)
pt.click()

for i in range(z,k):
    pt.typewrite(word)
    pt.press("enter")
    sent = sent + 1
    print("Sent %s Messages!"%(sent))
    time.sleep(delay)
