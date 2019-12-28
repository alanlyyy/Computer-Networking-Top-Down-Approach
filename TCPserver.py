from socket import *

serverPort = 12000

#initialize TCP connection handshake
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))

#wait for client to establish a connection with server
serverSocket.listen(1)

print("The server is ready to receive")

while 1:
    
    #create connection socket with client
    connectionSocket, addr = serverSocket.accept()
    
    
    sentence = connectionSocket.recv(1024)
    
    capitalizedSentence = sentence.upper()
    
    connectionSocket.send(capitalizedSentence)
    
    connectionSocket.close()