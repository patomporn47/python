#!/usr/bin/env python
# import os
# import sys
def chang_hostname(hostname):
	h = int(hostname)
	# os.system("hostnamectl set-hostname "(h))
	# os.system("hostnamectl status")
	print(type(h))
	print(h)

hostname= input("enter your hostname: ")
chang_hostname(hostname)