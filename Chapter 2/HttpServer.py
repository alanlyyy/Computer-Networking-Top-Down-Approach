from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)

print "\n" + gethostbyname(gethostname())

serverName = " "
serverPort = 80


#listen and bind to client
serverSocket.bind(("",serverPort))

#connect to one host only
serverSocket.listen(1)

while True:
    
    #Establish connection 
    print("\n\n Ready to serve...")
    
    connectionSocket, address = serverSocket.accept()
    
    try:
        
        #Receive HTTP request from browser
        message = connectionSocket.recv(1024)
        print("\n %s" %message)
        
        #open file mentioned in the first line of the HTTP request header
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        
        #Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n")
        
        #Send the conect of the requested file to the client
        connectionSocket.send(outputdata)
        connectionSocket.close()
    
    except IOError:
    
        #Send response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n")
        
        #Close client socket
        connectionSocket.close()

serverSocket.close()