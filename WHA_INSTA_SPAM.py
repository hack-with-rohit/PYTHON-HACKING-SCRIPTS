""" The code is developed for Educational Purpose Only , learn and hack yourself
                      --> BY HACK WITH ROHIT TAMIL"""

import pyautogui, time
import pyfiglet

msg = pyfiglet.figlet_format("Hack With Rohit")
print(msg)
filename = input("Enter the path to wordlist : ")
time.sleep(5)


f = open(filename,'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    
