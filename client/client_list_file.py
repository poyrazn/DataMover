#!/usr/bin/env python
# client_list_file
# DataMover
#
# Created by Nehir Poyraz on 10.11.2018

import socket
import os
import sys

#HOST = '10.0.2.15'
HOST = 'localhost'
PORT = 1111
ADDR = (HOST, PORT)
BUFSIZE = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(ADDR)
machine = socket.gethostname()


if __name__ == '__main__':
    user = os.getlogin()
    sock.send(user)
#    sock.shutdown(socket.SHUT_WR)
    data = sock.recv(BUFSIZE)
    print(data)



