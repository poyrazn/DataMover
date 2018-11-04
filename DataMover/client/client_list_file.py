#
# client_list_file
# DataMover
#
# Created by Nehir Poyraz on 28.10.2018
# Copyright  2018 Nehir Poyraz. All rights reserved.

import sys
import os
from socket import *
PORT = 1111
HOST = '10.0.2.15'
ADDR = (HOST, PORT)
sock = socket(AF_INET, SOCK_STREAM)
sock.connect(ADDR)


def list():
    NotImplemented


if __name__ == '__main__':
    sock.send("Connected")
    print("Connected from:", sock.getsockname())
    print("Connected to:", sock.getpeername())
    while True:
        print("waiting")
        result = sock.recv(1024)
        print(result)
        sock.send('foo')
        print("Sent: foo")
        if result == 3:
            break