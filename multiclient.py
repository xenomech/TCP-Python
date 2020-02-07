import socket
s=socket.socket()
port=input("enter port no:")
port=1123
s.connect(('127.0.0.1',port))
while (1):
     msg=s.recv(1024)
     if(msg == 'exit'):
        break;
     print msg
     
     
     
     

