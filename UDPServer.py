from socket import *

serverPort = 12000

#SOCK_DGRAM indicates udp transport
serverSocket = socket(AF_INET, SOCK_DGRAM)

#bind to port number 12000 for incoming connection
serverSocket.bind(('', serverPort))

print(" The server is ready to receive")

while True:
    
    #recieve the input from client
    message, clientAddress = serverSocket.recvfrom(2048)
    
    #convert bytes to string
    message = message.decode()
    
    modifiedMessage = message.upper()
    
    print(modifiedMessage)
    
    #send the modified message back to client
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)