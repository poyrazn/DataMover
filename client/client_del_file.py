#!/usr/bin/python2.7
#
# client_del_file
# DataMover
#
# Created by Nehir Poyraz on 11.11.2018

import socket
import os
import sys
import hashlib
import pickle
import logging


FORMAT ='%(asctime)-15s | %(levelname)s: DEL %(message)s'
logging.basicConfig(filename='client.log', level=logging.DEBUG, format=FORMAT, datefmt='%m/%d/%Y %H:%M:%S')
logger = logging.getLogger(__name__)

BUFSIZE = 4096

RED = '\033[91m'	# fail
GREEN = '\033[92m'	# success
LIGHTBLUE = '\033[96m'	# file already exists
YELLOW = '\033[93m'	# request sent
END = '\033[0m'



def newsocket():
	HOST = 'localhost'
	PORT = 4444
	ADDR = (HOST, PORT)
	newsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	newsocket.connect(ADDR)
	logger.info('Connected to server.')
	return newsocket


def send(request, sock):
	pickled = pickle.dumps(request, pickle.HIGHEST_PROTOCOL)
	pickled += b'\n'
	sock.send(pickled)
	sock.shutdown(socket.SHUT_WR)

	
def receive(sock):
	pickled = sock.recv(BUFSIZE)
	pickled = b''+pickled
	reply = pickle.loads(pickled)
	sock.shutdown(socket.SHUT_RD)
	return reply
	
def checksum(path, opt):
	md5 = hashlib.md5()
	with open(path, 'r') as f:
		content = f.read()
	md5.update(content.encode('utf-8'))
	if opt == 'check':
		return md5.hexdigest(), len(content)
	if opt == 'transfer':
		return content, md5.hexdigest(), len(content)

	
def check(path):
	try:
		os.path.exists(path)
		md5, filesize = checksum(path, 'check')
		request = {'type': 'check', 'username': os.getlogin(), 'filename': sys.argv[1],'md5': md5, 'filesize': filesize}
		logger.info('Requested file ' + request['filename'])
		return request
	except:
		print(RED +'File delete is not permitted. Please provide an existing file.'+ END)
		logger.error(request['filename'] + ' File not found.')
		logger.info('Abort transfer request.')
		sys.exit(0)
	

if __name__ == '__main__':
	
	if len(sys.argv) == 1:
		print('Please provide a file to transfer.')
	else:
		filename = sys.argv[1]
		filepath = os.getcwd() + '/' + filename
		request = check(filepath)
		sock = newsocket()
		send(request, sock)
		reply = receive(sock)
		sock.close()
		if reply['status'] == 200:
			print(GREEN + reply['message'] + END)
		else:
			print(RED + reply['message'] + END)
		logger.info(request['filename'] + ' ' +  reply['message'])
