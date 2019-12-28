from socket import *

serverName = "serverName"
serverPort = 12000

#create socket using TCP protocol
clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName,serverPort))

sentence = input("Input lowercase sentence:")

#send encoded data to server
clientSocket.send(sentence.encode())

#receive data fromn server
modifiedSentence = clientSocket.recv(1024)

print( "From Server: " , modifiedSentence)

clientSocket.close()