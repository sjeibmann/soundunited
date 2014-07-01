#!/usr/bin/python

import time as time
import subprocess

# val = 10
t = str(time.ctime())
try:
	log = open('/home/pi/logs/log.txt','a')
except:
	subprocess.call("touch logs/log.txt", shell=True)

def main(*arg):
	log.write("(" + t + ",")
	for n in range(len(arg)):
		log.write(str(arg[n]))
		if n != len(arg)-1:
			log.write(",")
	log.write(")" + '\n')

if __name__ == "__main__":
	import sys
	try:
		try:
			log = open('/home/pi/logs/log.txt','a')
		except:
			subprocess.call("touch logs/log.txt", shell=True)
		main(sys.argv[1:])
	except:
		print "No arguments to record."
