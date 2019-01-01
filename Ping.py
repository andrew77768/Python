import os

print ("Please enter the hostname/IP address:")
hostname = input()
response = os.system("ping -w 10 " + hostname)

if result == 0:
  print 'machine is online!'
else:
  print 'machine is offline!'
