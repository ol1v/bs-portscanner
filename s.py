#!/bin/python

import sys
import socket
from datetime import datetime

#Define target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])

else:
	print("format: python3 scanner.py <ip>")

print("Scanning target" + target)

#try open ports

try: 
	for port in range(50,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port)) #returns error
		
		if result == 0:
			print("Port {} is open".format(port))
		s.close()

except KeyboardInterrupt:
	print("\n Exiting Program")
	sys.exit()

except socket.gaierror:
	print("Hostname could not be resolved.")

except socket.error:
	print("Couldn't connect to server.")
	sys.exit()


