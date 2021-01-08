# Bhavik Patel
# Communication Network Project
# run python 3.8 version

import sys
import socket

# UDP Connection
# Extracts the arguments/parameters given with python commandline
UDPServerAddress = sys.argv[1]
UDPServerPort = sys.argv[2]
msgFromClient = sys.argv[3]

# Convert message to bytes and setup UDP server address & port
bytesToSend = str.encode(msgFromClient)
UDPServerAddressPort = (UDPServerAddress, int(UDPServerPort))
bufferSize = 1024

# Create UDP client socket and send message to the server
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPClientSocket.sendto(bytesToSend, UDPServerAddressPort)

# Extract message received from the UDP server
msgFromUDPServer = UDPClientSocket.recvfrom(bufferSize)
print("UDP data sent: " + msgFromClient)
print("UDP data received: {}".format(msgFromUDPServer[0].decode("utf-8")))

# Split the Server Address and port received from UDP server
TCPServerAddress, TCPServerPort = msgFromUDPServer[0].decode("utf-8").split(" ", 1)
print("TCP server: " + TCPServerAddress)
print("TCP port: " + TCPServerPort)

# TCP Connection
# Create TCP socket and connect to the server
TCPSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TCPServerAddressPort = (TCPServerAddress, int(TCPServerPort))
TCPSocket.connect(TCPServerAddressPort)

# Send initial message 'hello' to the TCP server
msgFromClient = "hello"
print("TCP data sent: " + msgFromClient)
TCPSocket.sendall(str.encode(msgFromClient))
msgFromTCPServer = TCPSocket.recv(bufferSize)
print("TCP data received: " + msgFromTCPServer.decode("utf-8"))

# Once connection is established get input from terminal/console and send it to TCP server
while True:
    print("Next message to send?")
    msgFromClient = str(input())
    # if command line input is quit then close connection
    if msgFromClient == 'quit' or msgFromClient == '"quit"' or msgFromClient == "'quit'":
        print('closing connection, goodbye')
        TCPSocket.close()
        break
    # else keep asking for input from terminal
    else:
        TCPSocket.sendall(str.encode(msgFromClient))
        print("TCP data sent: " + msgFromClient)
        msgFromTCPServer = TCPSocket.recv(bufferSize)
        print("TCP data received: " + msgFromTCPServer.decode("utf-8"))
