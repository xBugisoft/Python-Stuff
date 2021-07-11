import pyautogui
import keyboard
import time
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#X:  320 Y:  539 RGB: ( 33, 104,  33) #Green
#X:  511 Y:  541 RGB: (172, 165,  32) #Yellow
#X:  317 Y:  740 RGB: ( 26,  26, 166) #Blue
#X:  508 Y:  735 RGB: (169,  29,  29) #Red

def colorcheck(x,listen):
    if pyautogui.pixel(320,539) [0] != 33:
        while pyautogui.pixel(320,539) [0] != 33:
            time.sleep(0.05)
        print("#Press: Green #")
        x+=1
        if x > len(color_to_press):
            color_to_press.append(1)
            listen = False

    if pyautogui.pixel(511,541) [0] != 172:
        while pyautogui.pixel(511,541) [0] != 172:
            time.sleep(0.05)
        print("#Press: Yellow#")
        x+=1
        if x > len(color_to_press):
            color_to_press.append(2)
            listen = False

    if pyautogui.pixel(317,740) [0] != 26:
        while pyautogui.pixel(317,740) [0] != 26:
            time.sleep(0.05)
        print("#Press: Blue  #")
        x+=1
        if x > len(color_to_press):
            color_to_press.append(3)
            listen = False

    if pyautogui.pixel(508,735) [0] != 169:
        while pyautogui.pixel(508,735) [0] != 169:
            time.sleep(0.05)
        print("#Press: Red   #")
        x+=1
        if x > len(color_to_press):
            color_to_press.append(4)
            listen = False

    return x,listen

color_to_press = []

x = 0
listen = True

while 1:
    if keyboard.is_pressed('q'):
        while 1:
            if listen:
                x,listen = colorcheck(x,listen)
            else:
                for number in color_to_press:
                    if number == 1:
                        click(320,539)
                        
                    if number == 2:
                        click(511,541)
                        
                    if number == 3:
                        click(317,740)
                        
                    if number == 4:
                        click(508,735)

                time.sleep(0.2)
                print('#Done, next   #')
                listen = True
                x=0
