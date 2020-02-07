import socket
from threading import Thread
def send():
	while(1):
		msg = raw_input()
		c.send(msg)
		if msg == 'stop':
			print "Connection Terminated"
			break			
def recv():
	while(1):
		msg=c.recv(1000)
		print 'ser - >'+msg
		if msg == 'stop':
			#print "Connection Terminated"
			break
port = 1235

c = socket.socket()
c.connect(('127.0.0.1',port))

t1=Thread(target=send)
t1.start()
t2=Thread(target=recv)
t2.start()

