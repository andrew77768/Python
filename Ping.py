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
response = os.system("ping -w 10 " + hostname)

if result == 0:
  print 'machine is online!'
else:
  print 'machine is offline!'
