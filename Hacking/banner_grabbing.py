import socket 
import sys

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

for host in range(80, 100):
	    ports = open('ports.txt', 'r')
	    vulnbanners = open('vulnbanners', 'r')
	    for port in ports:
	    	    try:
	    	    	    socket.connect(( str(sys.argv[1]+'.'+str(host)), int(port) ))
	    	    	    print 'Connecting to '+str(sys.argv[1]+'.'+str(host))+' in the port: '+str(port)
	    	    	    socket.settimeout(1)
	    	    	    banner = socket.recv(1024)
	    	    	    for vulbanner in vulbanners:
	    	    	    	   if banner.strip() in vulbanner.strip():
	    	    	    	           print 'We have a winner! '+banner
	    	    	    	           print 'Host: '+str(sys.argv[1]+'.'+str(host))
	    	    	    	           print 'Port: '+str(port)
	    	    except :
	    	    	    print 'Error connecting to: '+str(sys.argv[1]+'.'+str(host)) +':'+ str(port)
	    	    	    pass 