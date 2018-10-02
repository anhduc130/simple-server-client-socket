import socket
import random
import time

UDP_IP = 'localhost'
UDP_PORT = 12000

# Set up the UDP server socket
serverSocket = socket.socket(socket.AF_INET,    # Internet
                             socket.SOCK_DGRAM) # UDP protocol

# Listen to the IP and PORT for clients
serverSocket.bind((UDP_IP, UDP_PORT))

while True:
    # Receive a message from the client
    (data, address) = serverSocket.recvfrom(1024)

    # Pick a random delay timing
    randomDelayTime = random.randint(5, 50) / 1000

    # Pick a random packet loss rate
    randomLossRate = random.uniform(0, 1)
    print ('loss rate: ' + str(randomLossRate))

    # If packet is not lost (rate > 10%)
    if randomLossRate > 0.1:
        # Simulate variability of delay
        time.sleep(randomDelayTime)

        # Echo back the received message
        serverSocket.sendto(data, address)
