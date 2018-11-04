#
# server_xinetd_list
# DataMover
#
# Created by Nehir Poyraz on 28.10.2018
# Copyright © 2018 Nehir Poyraz. All rights reserved.


import os
import sys
import socket

HOST = ''  # The variable of HOST is null, so the function bind( ) can be bound to all valid addresses.
PORT = 21567
BUFSIZ = 1024  # Size of the buffer
ADDR = (HOST, PORT)
sersock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sersock.bind(ADDR)
if __name__ == '__main__':
    while True:
        clisock, addr = sersock.accept()
        while True:
            data = clisock.recv(BUFSIZ)
            print("Received", data)
            sent = sersock.send("Foo")
            print("Sent", sent)
            # directory = '/Users/nehir/Desktop/test'
            # if os.path.exists(directory) and os.path.isdir(directory):
            #     dirs = os.scandir(directory)
            #     if not dirs:
            #         print("There are no stored files.", flush=True)
            #     else:
            #         print('ls -la')
            #
            # else:
            #     try:
            #         os.makedirs(directory)
            #         print("Data directory is created.")
            #     except OSError:
            #         print('Error: Directory couldn\'t been created. ' + directory)
