#https://docs.python.org/3/library/sys.html#sys.platform

import os
import socket 
import sys
import split

print ("Please enter the hostname/IP address you'd like to check:")
Hostname_tocheck = input()
Hostname_tocheckIP = socket.gethostbyname(Hostname_tocheck)


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
  print(Hostname_tocheck,"/",Hostname_tocheckIP, "is online!")
else:
  print(Hostname_tocheck,"/",Hostname_tocheckIP, "is offline!")

