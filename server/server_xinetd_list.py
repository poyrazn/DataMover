#!/usr/bin/python2.7
#
# server_xinetd_list
# DataMover
#
# Created by Nehir Poyraz on 10.11.2018


import os
import sys
import logging

if __name__ == '__main__':

    username = sys.stdin.readline().strip()
    if len(username):
        path = '/home/DataCloud/' + username
        if not os.path.isdir(path):
            os.mkdir(path)
            sys.stdout.write('202, Data directory ' + path + ' is created.')
        else:
            if not os.listdir(path):
                #print('204, Data directory is empty.')
                sys.stdout.write('204, Data directory is empty.')
            else:
                os.system('ls -la ' + path)
		sys.stdout.flush()
