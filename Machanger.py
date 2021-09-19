import time
import subprocess

interface = input("Enter your prefered interface(wlan0,eth0): ")
print("The interface you have chosen is " + interface)
mac_address = input('Enter you custom mac must start with 00: and 6 octets: ')

print("Changing Mac to " + mac_address + " for " + interface)
time.sleep(1)
print("10% =======")
time.sleep(1)
print("40% ===========")
time.sleep(1)
print("70% =============")
time.sleep(1)
print("100% ===============")
time.sleep(1)
print("Successfully Changed")

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + mac_address, shell=True)
subprocess.call("ifconfig " + interface + " up " , shell=True)

