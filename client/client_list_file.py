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
FORMAT ='%(asctime)-15s | %(levelname)s: %(message)s'
logging.basicConfig(filename='client.log', level=logging.DEBUG, format=FORMAT, datefmt='%m/%d/%Y %H:%M:%S')
logger = logging.getLogger(__name__)
logger.info('First message')
print(logger)

# establish connection
HOST = 'localhost'
PORT = 1111
ADDR = (HOST, PORT)
BUFSIZE = 4096
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(ADDR)
log = 'Connected to server.'

# handle request

sock.send(username)
sock.shutdown(socket.SHUT_WR)
data = sock.recv(BUFSIZE)
print(data)



