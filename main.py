# BonziWORLD Server Maker

# This program will help you set up a server for your BonziWORLD game.

# First, we'll need to import the necessary modules:

import socket # For creating a socket connection

import sys # For system-specific parameters and functions

# Now, let's create the socket:

try:

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print("Socket successfully created")

except socket.error as err:

    print("Socket creation failed with error %s" %(err))

# Now, let's bind the socket to a port:

port = 8888 # This is the port we'll use for the BonziWORLD server

try:

    s.bind(('', port))

    print("Socket binded to %s" %(port))

except socket.error as err:

    print("Socket bind failed with error %s" %(err))

# Now, let's set the socket to listen:

s.listen(5)

print("Socket is now listening")

# Now, let's create a loop that will accept incoming connections:

while True:

    # Establish connection with client

    c, addr = s.accept()

    print("Got connection from", addr)

    # Send a message to the client

    c.send("Welcome to BonziWORLD! Please enter your username and password to log in".encode('utf-8'))

    # Receive data from the client

    data = c.recv(1024).decode('utf-8')

    print("Received data:", data)

    # Now, let's check the username and password:

    username = data.split(',')[0]

    password = data.split(',')[1]

    if username == "admin" and password == "admin":

        c.send("Login successful!".encode('utf-8'))

    else:

        c.send("Login failed!".encode('utf-8'))

    # Close the connection

    c.close()
