#!/usr/bin/python2.7
#
# client_put_file
# DataMover
#
# Created by Nehir Poyraz on 11.11.2018

from __future__ import print_function
import socket
import os
import sys
import hashlib

HOST = 'localhost'
PORT = 1111
ADDR = (HOST, PORT)
BUFSIZE = 4096
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(ADDR)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Please provide a file to be transferred.')
    else:
        filename = sys.argv[1]
        filepath = os.getcwd() + '/' + filename
        if os.path.exists(filepath):
            md5 = hashlib.md5()
            with open(filepath) as f:
                content = f.read()
                md5.update(content)
            filesize = os.path.getsize(filepath)
            username = os.getlogin()
            sock.send(username)
            sock.send(filename)
            sock.send(md5.digest())
            sock.send(str(filesize))
            sock.send(content)
            sock.shutdown(socket.SHUT_WR)
            status = sock.recv(BUFSIZE)
            print(status)
        else:
            print('File does not exists.')





