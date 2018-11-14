#!/usr/bin/python2.7
#
# client_list_file
# DataMover
#
# Created by Nehir Poyraz on 10.11.2018

import socket
import os
import logging
import pickle


FORMAT ='%(asctime)-15s | %(levelname)s: LIST %(message)s'
logging.basicConfig(filename='client.log', level=logging.DEBUG, format=FORMAT, datefmt='%m/%d/%Y %H:%M:%S')
logger = logging.getLogger(__name__)

BUFSIZE = 4096

RED = '\033[91m'	# fail
GREEN = '\033[92m'	# success
LIGHTBLUE = '\033[96m'	# file already exists
YELLOW = '\033[93m'	# request sent
END = '\033[0m'

# establish connection
HOST = 'localhost'
PORT = 1111
ADDR = (HOST, PORT)
BUFSIZE = 4096

def connect():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect(ADDR)
	return sock

def receive(sock):
	pickled = sock.recv(BUFSIZE)
	pickled = b'' + pickled
	reply = pickle.loads(pickled)
	sock.shutdown(socket.SHUT_RD)
	return reply

def check(reply):
	if reply[:3] == '202' or reply[:3] == '204':
		reply = reply.split(',')
		message = reply[1]
		if reply[0] == '202':
			logger.info(message)
			print(GREEN + message + END)
		else:
			print(reply[0])
			logger.info(message)
			print('-' * 70 + RED + '\nThere are no stored files.\n' + END + '-' * 70 )
	else:
		logger.info('Data directory is listed.')
		print(reply)

sock = connect()
logger.info('Connected to server.')
username = os.getlogin()
sock.send(username)
sock.shutdown(socket.SHUT_WR)
reply = sock.recv(BUFSIZE)
check(reply)





