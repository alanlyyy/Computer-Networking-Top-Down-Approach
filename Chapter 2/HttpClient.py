"""
First step is to install a web server on a different host.
Create html file in the root directory of the web server
Send a GET message to the IP address of your web server to extract the html file.

How to install Apache web server 2
https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-18-04-quickstart

"""

from socket import *

#Get server host IP address and port number
serverIP = "your_server_IP"
serverPort= 80

#create socket
clientSocket = socket(AF_INET,SOCK_STREAM)

try:
    #Try connecting to the provided host
    clientSocket.connect((serverIP,serverPort))
    
    print("Connection Successful.")
    
    #get the fileName
    #fileName = input("Enter the relative path of the file to be retrieved : ")
    fileName = "index.html"
    
    #encode HTTP strings as bytes and send over data stream to web server
    clientSocket.send( ("GET /" + fileName + " HTTP/1.1\r\n" +
                       "Host: " + gethostbyname(gethostname()) + ":" + str(clientSocket.getsockname()[1]) + "\r\n\r\n").encode())
    
                        
    print("\n\n----------------------HTTP Response------------------\n")
    
    #Receive one HTTP response header line
    response = clientSocket.recv(1024)
    print(response)
    
    #Receive the file 
    fileData = clientSocket.recv(10000)
    
    print(fileData)
    
    print("-----------------END of HTTP Response--------------- \n")
    
    #close connection socket
    clientSocket.close()
    
except error:
    
    print("\n\nError while connecting!")
    
    clientSocket.close()