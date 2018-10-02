import socket
import time

UDP_IP = 'localhost'
UDP_PORT = 12000
MESSAGE = "PING"

# Set up the UDP client socket
clientSocket = socket.socket(socket.AF_INET,    # Internet
                             socket.SOCK_DGRAM) # UDP protocol

# Set timeout on socket blocking operations (e.g recvfrom())
clientSocket.settimeout(1)

i = 1
while (i <= 10):
    # Time at which the message is sent to the server 
    initialTime = time.time()

    # Send the message to the server
    clientSocket.sendto((MESSAGE + ' ' + str(i)).encode('utf8'), (UDP_IP, UDP_PORT))

    try:
        # Receive the echoed message from the server
        (data, address) = clientSocket.recvfrom(10)

        # Calculate RTT time after receiving the echoed message
        RTT = time.time() - initialTime

        # Print the RTT result and the received message
        print (str(RTT) + ' ' + data.decode('utf8'))
    except socket.timeout:
        # If not hear back from the server after 1 second, the request timed out
        print ('Request Timeout')

    # Increment the counter to the next request
    i = i + 1
