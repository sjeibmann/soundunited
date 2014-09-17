import os
import sys

path = "/home/pi/logs/now_playing.fifo"
fifo = open(path, "r")
for line in fifo:
    print "Received: " + line,
fifo.close()