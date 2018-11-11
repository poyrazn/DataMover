#!/usr/bin/python2.7
#
# server_xinetd_put
# DataMover
#
# Created by Nehir Poyraz on 11.11.2018

from __future__ import print_function
import os
import time
import sys
import hashlib

if __name__ == '__main__':
    md5 = hashlib.md5()
    username = sys.stdin.readline().strip()
    path = '/home/DataCloud/' + username + '/'
    filename = sys.stdin.readline().strip()
    filepath = path + filename
    clientmd5 = sys.stdin.readline().strip()
    filesize = int(sys.stdin.readline().strip())
    content = sys.stdin.read()

    print("File " + filename + " transmission for path " + filepath)
    sys.stdout.flush()

    """if os.path.exists(filepath):
        with open(filepath) as f:
            md5.update(f.read().encode('utf-8'))
        print('\033[93mFile' + filename + ' exists. Calculating MD5 checksum.\033[0m', flush=True)
        if clientmd5 == md5.digest():
            print('\033[92mFile ' + filename + ' is succesfully recorded. MD5 checksum passed.\033[0m', flush=True)
        else:
            print('\033[91mFile is either corrupted, interrupted or outdated.\033[0m', flush=True)

    else:
        print('\033[94m' + filename + ' is being stored...', flush=True)
        starttime = time.ctime()
        f = open(filepath, 'w')
        endtime = time.ctime()
        for i in range(100):
            print ('=', end='', flush=True)
        print('100 % Complete! (', endtime-starttime, 'secs )\033[0m', flush=True)
        f.write(content)
        f.close()
        with open(filepath) as f:
            md5.update(f.read())
        if clientmd5 == md5.digest():
            print('\033[92mFile ' + filename + ' is succesfully recorded. MD5 checksum passed.\033[0m', flush=True)
        else:
            print('\033[91mTransmission failed. Retry recommended.\033[0m', flush=True)"""
