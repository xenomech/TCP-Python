import socket

port=1234
s=socket.socket()
#s.bind(('172.16.104.12',port))
s.bind(('127.0.0.1',port))
s.listen(3)
while(1):
	msg=raw_input("Enter the Message:")
	c,addr=s.accept()
	c.send(msg)
	if msg == 'stop':
		break
	msg = s.recv(1000)
	print msg
	if msg == 'stop':
		break
s.close()
