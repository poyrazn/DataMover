#!/usr/bin/python2.7
#
# client_put_file
# DataMover
#
# Created by Nehir Poyraz on 11.11.2018

import socket
import os
import sys

HOST = 'localhost'
PORT = 1111
ADDR = (HOST, PORT)
BUFSIZE = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(ADDR)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Please provide a file to be transferred.')
    else:
        with open(sys.argv[0]) as f:
            content = f.read()
    sock.send(content)
    sock.shutdown(socket.SHUT_WR)
    data = sock.recv(BUFSIZE)
    print(data)