import socket
client_socket = socket.socket()
client_socket.connect((('127.0.0.1',1090)))
message = raw_input(" -> ")
while message.lower().strip() != 'bye':
	client_socket.send(message)
	data = client_socket.recv(1024)
	print('Received from server: ' + data)
	message = raw_input(" -> ")
client_socket.close()
