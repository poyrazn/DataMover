#!/usr/bin/python2.7
#
# client_list_file
# DataMover
#
# Created by Nehir Poyraz on 10.11.2018

import socket
import os
import logging

username = os.getlogin()

# establish connection
HOST = 'localhost'
PORT = 1111
ADDR = (HOST, PORT)
BUFSIZE = 4096
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(ADDR)

# handle request

sock.send(username)
sock.shutdown(socket.SHUT_WR)
data = sock.recv(BUFSIZE)
print(data)



