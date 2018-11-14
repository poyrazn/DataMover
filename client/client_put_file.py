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
PORT = 2222
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
	pickled = b'' + pickled
	reply = pickle.loads(pickled)
	sock.shutdown(socket.SHUT_RD)
	return reply
	

def checksum(path):
	md5 = hashlib.md5()
	with open(path, 'r') as f:
		content = f.read()
	md5.update(content.encode('utf-8'))
	return content, md5.hexdigest(), len(content)

	
def request(File, mode):
	if os.path.exists(File):
		data, md5, filesize = checksum(File)
		if mode == 'check':
			request =  {'type': mode, 'username': os.getlogin(), 'filename': sys.argv[1],'md5': md5, 'filesize': filesize}
		if mode == 'transfer':
			request =  {'type': mode,'username': os.getlogin(), 'filename': sys.argv[1], 'md5': md5, 'filesize': filesize , 'data' : data}
		sock = connect()
		send(request, sock)
		reply = receive(sock)
		sock.close()
	else:
		print(RED + 'File does not exists. Please provide an existing filename.' + END)
		sys.exit(0)
	return reply

def check(reply):
	if reply['status'] == 200:
		print(GREEN + reply['message'] + END)
		sys.exit(0)
	else:
		if reply['status'] == 404:
			print(RED + reply['message'] + END)
		elif reply ['status'] == 500:
			print(RED + reply['message'] + END)
			sys.exit(0)
		else:
			print(YELLOW + reply['message'] + END)
		return True
		

if __name__ == '__main__':
	
	if len(sys.argv) == 1:
		print('Please provide a file to transfer.')
	else:
		File = os.getcwd() + '/' + sys.argv[1]
		reply = request(File, 'check')
		if check(reply):
			reply = request(File, 'transfer')
			check(reply)
			

		

        	
            



