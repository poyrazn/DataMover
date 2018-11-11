#!/usr/bin/env python
#
# server_xinetd_list
# DataMover
#
# Created by Nehir Poyraz on 10.11.2018

import os
import sys

if __name__ == '__main__':

    buffer = sys.stdin.readline().strip()
    username = ''
    if len(buffer):
        username += buffer
    path = '/home/DataCloud/' + username
    print('Looking for directory:', username)
    sys.stdout.flush()
    if not os.path.isdir(path):
        os.mkdir(path)
        print('Data directory is created.')
        sys.stdout.flush()
    else:
        if not os.listdir(path):
            print('-' * 70 + '\n\033[0;31;40m There are no stored files\033[0;37;40m\n' + '-' * 70)
            sys.stdout.flush()
        else:
            os.system('ls -la ' + path)
            sys.stdout.flush()
     # Flush the standard output, so the message is sent.
