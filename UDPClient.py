from socket import *

serverName = '192.168.1.164'
serverPort = 12000

#create socket
clientSocket = socket(AF_INET,SOCK_DGRAM)
message = input('Input lowercase sentence:').encode()

#write message to socket 
clientSocket.sendto(message,(serverName, serverPort))

#recieve message back from server
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

print(modifiedMessage.decode())

clientSocket.close()