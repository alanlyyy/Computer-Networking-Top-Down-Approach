"""Need to enable firewall for specific port in order for server to allow for incoming data,
otherwise program will stall

"""

# UDPPingerServer.py
# We will need the following modules to generate randomized lost packets import random
from socket import *
import random
import time

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM) # Assign IP address and port number to socket
serverSocket.bind(("", 12000))

while True:
    # Generate random number in the range of 0 to 10
    rand = random.randint(0, 10)

    # Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(1024)
    
    
    # Capitalize the message from the client
    message = message.decode() + "Received"

    # If rand is less is than 4, we consider the packet lost and do not respond
    if rand < 6:
    
        #add delay of 1seconds to simulate lost package
        time.sleep(1)
        
        #go back to start of loop
        continue

    # Otherwise, the server responds
    serverSocket.sendto(message.encode(), address)