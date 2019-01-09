import os
import socket 
import sys

outcome = 0

#Debug Mode, to test and all
def Debug_Mode():
    Local_Hostname = socket.gethostname()
    Local_IPAddress = socket.gethostbyname(Local_Hostname)
    
    print("System Platform:",sys.platform)
    #Below only work on a windows machine.
    print("Windows OS Version:",sys.getwindowsversion().major)
    print("Windows Version:",sys.winver)
    print("")
    
    print("IPV4 Address:",Local_IPAddress)
    print("Hostname:",Local_Hostname)
    print_test = socket.gethostbyaddr(Local_Hostname)
    print("Domain:",print_test[0])
    print("IPV6 Address:",print_test[2])
    print("")

#Call our debug mode
Debug_Mode()
