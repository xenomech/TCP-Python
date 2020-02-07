import socket
server_socket = socket.socket()
server_socket.bind(("127.0.0.1",1090))
server_socket.listen(2)
conn, address = server_socket.accept()
print("Connection from: " + str(address))
while True:
	data = conn.recv(1024)
	if not data:
		break
	print("from connected user: " + str(data))
	data = raw_input(' -> ')
	conn.send(data)
conn.close()
