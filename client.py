#import threading, socket



import socket
import threading

hostorjoin = input("Host a Server or Connect (H to Host, C to Connect): ")

nickname = input("Enter Nickname: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverip = input("Enter Server IP: ")
serverport = int(input("Enter Port: "))
client.connect((serverip,serverport))

def receive():
	while True:
		try:
			message = client.recv(1024).decode('ascii')
			if message == 'NICK':
				client.send(nickname.encode('ascii'))
			else:
				print(message)

		except:
			print("An Unknown Error Occured")
			client.close()
			break


def write():
	while True:
		message = "{}: {}".format(nickname, input())
		client.send(message.encode('ascii'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
