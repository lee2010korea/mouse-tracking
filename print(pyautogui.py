import pyautogui
import time
import os

while True:
    x, y = (pyautogui.position()) 
    os.system('cls')
    xx1 = int((x/100-1))
    xx2 = int(23-xx1+1)
    for n in range(int(y/100-1)):
        print(xx1*" ",0)    
    print(xx1*"0",1,xx2*"0")
    for n in range(int(14-y/100-1)):
        print(xx1*" ",0)
    time.sleep(0.00000000000000001)




