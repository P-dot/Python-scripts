#!/usr/bin/python

import telnetlib

HOST = "localhost"
tn = telnet.Telnet(HOST, "999")

tn.write("Hello Wotld\n")
print tn.read_all