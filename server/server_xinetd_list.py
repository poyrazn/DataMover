#!/usr/bin/python2.7
#
# server_xinetd_list
# DataMover
#
# Created by Nehir Poyraz on 10.11.2018


import os
import sys
import logging

FORMAT ='%(asctime)-15s | %(levelname)s: LIST %(message)s'
logging.basicConfig(filename='home/DataCloud/server.log', level=logging.DEBUG, format=FORMAT, datefmt='%m/%d/%Y %H:%M:%S')
logger = logging.getLogger(__name__)

if __name__ == '__main__':

    username = sys.stdin.readline().strip()
    if len(username):
        path = '/home/DataCloud/' + username
        if not os.path.isdir(path):
            os.mkdir(path)
            message = 'Data directory ' + path + ' is created.'
            sys.stdout.write('202,' + message )
            logger.info(message)
        else:
            if not os.listdir(path):
                #print('204, Data directory is empty.')
                message = 'Directory ' + path + ' is empty.'
                sys.stdout.write('204,' + message)
                logger.info(message)
            else:
                os.system('ls -la ' + path)
                message = 'Directory ' + path + ' is listed.'
                logger.info(message)
		sys.stdout.flush()
