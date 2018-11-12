#!/usr/bin/python2.7

import hashlib
import pickle
import sys
import socket

BUFSIZE = 4096

def receive(sock=None):
	if sock:
		pickled = sock.recv(BUFSIZE)
		pickled = b''+pickled
		reply = pickle.loads(pickled)
		print('Client Received')
		return reply
	else:
		pickled = sys.stdin.read()
		request = pickle.loads(pickled)
		print('Server Received')
		print(request)
		return request
		
def send(data, sock=None):
	pickled = pickle.dumps(data, pickle.HIGHEST_PROTOCOL)
	if sock:
		pickled += b'\n'
		sock.send(pickled)
		sock.shutdown(socket.SHUT_WR)
		print('Client Sent')
	else:
		sys.stdout.write(pickled)
		sys.stdout.flush()
		print('Server Sent')
	

def checksum(path, opt):
	md5 = hashlib.md5()
	with open(path, 'rb') as f:
		content = f.read()
	md5.update(content)
	if opt == 'check':
		return md5.digest(), len(content)
	if opt == 'transfer':
		return content, md5.digest(), len(content)
	
