#!/usr/bin/python2.7
#
# server_xinetd_list
# DataMover
#
# Created by Nehir Poyraz on 10.11.2018

from __future__ import print_function
import os
import sys
import logging

if __name__ == '__main__':

    username = sys.stdin.readline().strip()
    if len(username):
        path = '/home/DataCloud/' + username
        if not os.path.isdir(path):
            os.mkdir(path)
            print("Data directory is created.", flush=True)
        else:
            if not os.listdir(path):
                print('-' * 70 + '\n\033[91m There are no stored files\033[0m\n' + '-' * 70, flush=True)
            else:
                os.system('ls -la ' + path)
                sys.stdout.flush()
