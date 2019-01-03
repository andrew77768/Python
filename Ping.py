#https://docs.python.org/3/library/sys.html#sys.platform

import os
import socket 
import sys

#Debug Mode, to test and all
def Debug_Mode():
    Local_Hostname = socket.gethostname()
    Local_IPAddress = socket.gethostbyname(Local_Hostname)
    print ("System Platform:",sys.platform)
    #Below only work on a windows machine.
    print("Windows OS Version:",sys.getwindowsversion().major)
    print("Windows Version:",sys.winver)
    print("")
    print("IP:",Local_IPAddress)
    print("Hostname:",Local_Hostname)
    print("")

#Call our debug mode
Debug_Mode()

print ("Please enter the hostname/IP address you'd like to check:")
Hostname_tocheck = input()

if sys.platform.startswith('linux'):
    result = os.system("ping -c 10 " + Hostname_tocheck)
elif sys.platform.startswith('win32'):
    result = os.system("ping -w 10 " + Hostname_tocheck)
elif sys.platform.startswith('freebsd'):
    print("Sucks to be you!")
elif sys.platform.startswith('cygwin'):
    print("Sucks to be you!")
elif sys.platform.startswith('darwin'):
    print("Sucks to be you!")

if result == 0:
  print(Hostname_tocheck, "is online!")
else:
  print(Hostname_tocheck, "is offline!")

