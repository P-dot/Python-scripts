#!/usr/bin/python

import os, time 

x = "Welcome to Polymath's environment"
y = 0

while y <= len(x):
        os.system("clear")
        print x[:y]
        time.sleep(.2)
        y = y+1
