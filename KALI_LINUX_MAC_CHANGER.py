""" The code is developed for Educational Purpose Only , learn and hack yourself
                      --> BY HACK WITH ROHIT TAMIL"""

import subprocess 
import pyfiglet 

msg = pyfiglet.figlet_format("MAC spoofing is a Home Address !!!!")
print(msg)
i=input("Enter New Home Address to Fast Spoof : ")
subprocess.call(["ifconfig","wlan0","down"])
subprocess.call(["ifconfig","wlan0","hw","ether",i])
subprocess.call(["ifconfig","wlan0","up"])

print("Home address changed Successfully!!!")

