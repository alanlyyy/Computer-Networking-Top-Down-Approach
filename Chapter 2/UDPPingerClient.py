"""Need to enable firewall for specific port in 
order for server to allow for incoming data and client to allow for outgoing data,
otherwise program stalls.

"""

# UDPPingerServer.py
# We will need the following modules to generate randomized lost packets import random
from socket import *
import time

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
clientSocket = socket(AF_INET, SOCK_DGRAM) 

#set timeout to 0.5 second for client to not receive response from server
clientSocket.settimeout(0.5)

serverName = "your_ip_address"
serverPort = 12000

count = 0

while count!= 10:
    
    #start measuring time
    start = time.time()

    #send ints (1-10) to socket 
    clientSocket.sendto(str(count).encode(),(serverName, serverPort))
    
    #if timeout exception is thrown start is reinitialized
    try:
        # Receive the server response along with the address it is coming from
        message, address = clientSocket.recvfrom(1024)
        
        #increase count
        count += 1
    except timeout:
        continue
    
    end = time.time()
    
    #measure elasped time
    elasped = end - start
    
    print(message,"elsapsed time: ", elasped)
