"""
HTTPProxyServer and HTTPServer will run on one unit with 2 different command prompts utilizing different ports.
HTTPclient will run on another unit.

Proxy server acts as a bypass for information between client and origin server.

The client sends HTTP request to Proxy server which sends the same HTTP request to origin server,
afterwards origin server sends the HTTP response + file contents to proxy server and back to client.

"""

from socket import *

serverName = ""
serverPort = 80

originName = "server_IP_address"
originPort = 8000

#server which acts as a bypass for client -> OriginServerSocket
ProxyServerSocket = socket(AF_INET, SOCK_STREAM)

#listen and bind to client
ProxyServerSocket.bind(("",serverPort))

#connect to one host only
ProxyServerSocket.listen(1)

while True:
    
    #Establish connection 
    print("\n\n Ready to serve...")
    
    #connect with client socket
    connectionSocket, address = ProxyServerSocket.accept()
    
    #server which contains the contents of the application side
    OriginServerSocket = socket(AF_INET,SOCK_STREAM)
    
    #Try connecting to the application host
    OriginServerSocket.connect((originName,originPort))
    
    print("OriginServerSocket Connection Successful.")
    
    #Receive HTTP request from client
    message = connectionSocket.recv(1024)
    print("\n %s" %message)
    
    #Send HTTP request line to originServer
    OriginServerSocket.send(message)
    
    #Receive one line HTTP response from origin server
    message = OriginServerSocket.recv(1024)
    
    #if file does not exist
    if message.decode() == "HTTP/1.1 404 Not Found\r\n":
    
        #Send one line HTTP response to client
        connectionSocket.send(message)
        
        #Close client socket
        connectionSocket.close()
    
        #close the client portion of the proxy server
        OriginServerSocket.close()
        
        #restart client and proxy server connections
        continue
        
    
    #Send one line HTTP response to client
    connectionSocket.send(message)
    
    
    #Receive the file from origin server
    fileData = OriginServerSocket.recv(10000)
    
    #send fileData to client
    connectionSocket.send(fileData)
        
    #server portion of proxy server close.
    connectionSocket.close()
    
    #close the client portion of the proxy server
    OriginServerSocket.close()
    

ProxyServerSocket.close()