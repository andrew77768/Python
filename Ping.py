import os

#https://docs.python.org/3/library/sys.html#sys.platform
import sys

#Debug Mode, to test and all
def debug():
    print (sys.platform)
    #Below only work on a windows machine.
    print (sys.winver)
    print (sys.getwindowsversion().major)

#Call our debug mode
debug()


print ("Please enter the hostname/IP address:")
hostname = input()

if sys.platform.startswith('linux'):
    result = os.system("ping -c 10 " + hostname)
elif sys.platform.startswith('win32'):
    result = os.system("ping -w 10 " + hostname)
elif sys.platform.startswith('freebsd'):
    print ("Sucks to be you!")
elif sys.platform.startswith('cygwin'):
    print ("Sucks to be you!")
elif sys.platform.startswith('darwin'):
    print ("Sucks to be you!")



if result == 0:
  print ("machine is online!")
else:
  print ("machine is offline!")
