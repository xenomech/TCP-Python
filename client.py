import socket
c=socket.socket()
port=1235

#c.connect(('172.16.104.12',port))
c.connect(('127.0.0.1',port))
msg=c.recv(1000)
print msg
