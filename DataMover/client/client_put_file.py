#
# client_put_file
# DataMover
#
# Created by Nehir Poyraz on 28.10.2018
# Copyright 2018 Nehir Poyraz. All rights reserved.

import hashlib
import os
import sys


BUFSIZ = 1024  # buffer size
PORT = 2222

"""HOST = '192.168.0.159'  # Server(Raspberry Pi) IP address


ADDR = (HOST, PORT)

"""


def put(file):
    """
    create a file on server
    :param file:
    :return:
    """
    global climd5
    """
    get file via stdin
    calculate MD5
    if file exists @server:
        calculate MD5 @server
        if MD5 checksum matches:
            "file exists"
        else:
            "file is found but either corrupted, interrupted or outdated."

        if filesize matches:
            (This is the current implementation.)
            transfer file / calculate MD5
        else:
            transfer file / calculate MD5
            if MD5 mathes:
                "file is succesfully stores"
            else:
                "store failed"
                "retry recommended"

    else:
        "file is being stored"
        transfer file / calculate MD5
        if MD5 mathes:
            "file is succesfully stores"
        else:
            "store failed"
            "retry recommended"
    """


if __name__ == '__main__':
    #connect to the server
    global climd5
    m = hashlib.md5()
    try:
        cmd, filename = sys.argv[0], sys.argv[1]
    except:
        print("No arguments given. Please provide a valid file name.")
    else:
        with open(filename) as file:
            content = file.read()


        m.update(content)
        climd5 = m.digest()
