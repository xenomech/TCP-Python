import socket
s=socket.socket()
port=input("enter port no:")
c=input("enter no: of clients")
port=1123
s.bind(('',port))
s.listen(5)
i=0
a=[]
for i in range(2):
	c,addr= s.accept()
	a.append(c)
i=0
while(1):
	msg=raw_input("enter message")
    	for i in range(2):
    		a[i].send(msg)
    	if(msg=="exit"):
       		break;
       		c.close()
       		s.close()


