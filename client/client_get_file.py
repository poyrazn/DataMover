#!/usr/bin/python2.7
#
# client_put_file
# DataMover
#
# Created by Nehir Poyraz on 11.11.2018

import socket
import os
import sys
import hashlib
import pickle



RED = '\033[91m'	# fail
GREEN = '\033[92m'	# success
LIGHTBLUE = '\033[96m'	# file already exists
YELLOW = '\033[93m'	# request sent
END = '\033[0m'


BUFSIZE = 4096
HOST = 'localhost'
PORT = 3333
ADDR = (HOST, PORT)


def connect():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect(ADDR)
	return sock


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
	

def checksum(File):
	md5 = hashlib.md5()
	with open(File, 'r') as f:
		content = f.read()
	md5.update(content.encode('utf-8'))
	return md5.hexdigest(), len(content)


def request(filename):
	request = {'username': os.getlogin(), 'filename': filename}
	sock = connect()
	send(request, sock)
	reply = receive(sock)
	sock.close()
	return reply


def check(reply):
	if reply['status'] == 404:
		print(RED + reply['message'] + END)
		sys.exit(0)
	else:
		return True
		


if __name__ == '__main__':
	
	if len(sys.argv) == 1:
		print('Please provide a filename to transfer.')
	else:
		File = os.getcwd() + '/' + sys.argv[1]
		reply = request(sys.argv[1])
		if check(reply):
			with open(File, 'wb') as f:
				f.write(reply['data'])
			md5, filesize = checksum(File)
			if reply['md5'] == md5 and reply['filesize'] == filesize:
				print(GREEN + 'File is succesfully transferred.' + END)
			else:
				print(RED + 'Contents may be corrupted, retry recommended.' + END)
				
			
		
		
			
			
