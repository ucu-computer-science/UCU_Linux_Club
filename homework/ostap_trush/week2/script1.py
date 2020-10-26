#!/bin/env python
# Return the ip adress of a user
import os

def return_ip():
	'''
	Returns user ip
	>>> return_ip()
	127.0.1.1
	'''
	ip = os.system("hostname -i")
return_ip()
