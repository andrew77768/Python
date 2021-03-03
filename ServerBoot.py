import requests
import sys
import socket
import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime

#Get Networking Information
Hostname = socket.gethostname()
IPv4 = socket.gethostbyname(Hostname) #internal

#external (Might need re-doing if IPV6 address includes "Current IP address text:" which gets stripped")
ext_ip = urllib.request.urlopen("http://checkip.dyndns.org")
soup = BeautifulSoup(ext_ip, features="html.parser")
ExternalIP2Strip = (next(soup.body.children))
StrippedExtIP = ExternalIP2Strip.strip("Current IP Address:")

#Date and time of boot
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

#Compile all data in prep for message
status = (
"A server has rebooted!" + 
"\nHostname: " + Hostname + 
"\nLocal IP is: " + IPv4 + 
"\nExternal IP: " + StrippedExtIP + 
"\nTime of reboot: " + dt_string + 
"\n"
)

r = requests.post("https://api.pushover.net/1/messages.json", data = {
#ServerBoot PushOver Application Token
"token": "AUTH TOKEN",
"user": "USER TOKEN",
"message": status #Can be a var also
})
print(r.text)
