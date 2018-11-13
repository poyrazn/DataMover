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


BUFSIZE = 4096

RED = '\033[91m'	# fail
GREEN = '\033[92m'	# success
LIGHTBLUE = '\033[96m'	# file already exists
YELLOW = '\033[93m'	# request sent
END = '\033[0m'


def newsocket():
	HOST = 'localhost'
	PORT = 2222
	ADDR = (HOST, PORT)
	newsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	newsocket.connect(ADDR)
	return newsocket


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
		return request
	except:
		print(RED +'File does not exists. Please provide an existing filename.'+ END)
		sys.exit(0)

def transfer(path, sock):
	data, md5, filesize = checksum(path, 'transfer')
	request = {'type': 'transfer','username': os.getlogin(), 'filename': sys.argv[1], 'md5': md5, 'filesize': filesize , 'data' : data}
	return request


if __name__ == '__main__':
	
	if len(sys.argv) == 1:
		print('Please provide a file to transfer.')
	else:
		filename = sys.argv[1]
		path = os.getcwd() + '/' + filename
		request = check(path)
		sock = newsocket()
		send(request, sock)
		reply = receive(sock)
		sock.close()
		if reply['status'] == 200:
			print(GREEN + reply['message'] + END)
		else:
			print(YELLOW + reply['message'] + END)
			print('Transfer protocol started')
			sock = newsocket()
			request = transfer(path, sock)
			send(request, sock)
			reply = receive(sock)
			sock.close()
			if reply['status'] == 200:
				print(GREEN + reply['message'] + END)
			else:
				print(RED + reply['message'] + END)

        	
            



