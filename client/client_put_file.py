#!/usr/bin/python2.7
#
# client_put_file
# DataMover
#
# Created by Nehir Poyraz on 11.11.2018

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


BUFSIZE = 2048

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
	print('pickling')
	print(b''+pickled)
	sock.send(pickled)
	sock.shutdown(socket.SHUT_WR)

	

def receive(sock):
	"""pickled = []
	while True:
		buf = sock.recv(BUFSIZE)
		pickled.append(buf)
		if len(buf) < BUFSIZE:
			break"""
	pickled = sock.recv(BUFSIZE)
	pickled = b''+pickled
	reply = pickle.loads(pickled)
	print('reply')
	print(reply)
	sock.shutdown(socket.SHUT_RD)
	return reply
	
	

def checksum(path, opt):
	md5 = hashlib.md5()
	with open(path, 'r') as f:
		content = f.read()
	md5.update(content.encode())
	if opt == 'check':
		return md5.hexdigest(), len(content)
	if opt == 'transfer':
		return content, md5.hexdigest(), len(content)

	
def check(path, sock):
	md5, filesize = checksum(path, 'check')
	request = {'username': os.getlogin(), 'filename': sys.argv[1],'md5': md5, 'filesize': filesize}
	print(request)
	print('Client Check')
	#request = {'username': 'nehir', 'filename': 'hello.txt','md5': 123, 'filesize': filesize}
	return request
	

def transfer(path, sock):
	print('transfer')
	data, md5, filesize = checksum(path, 'transfer')
	request = {'username': os.getlogin(), 'filename': sys.argv[1], 'data' : b'' + data , 'md5': b'' + md5, 'filesize': filesize}
	send(request, sock)
	reply = receive(sock)
	sock.close()
	return reply





if __name__ == '__main__':
	
	if len(sys.argv) == 1:
		print('Please provide a file to transfer.')
	else:
		filename = sys.argv[1]
		filepath = os.getcwd() + '/' + filename
		try:
			os.path.exists(filepath)
		except:
			print(RED +'File does not exists. Please provide an existing filename.'+ END)
		else:
			sock = newsocket()
			request = check(filepath, sock)
			#request = {'username': 'nehir', 'filename': 'hello.txt','md5': 123, 'filesize': 123}
			print(request)
			#send(request, sock)
			print('Client sent')
			send(request, sock)
			reply = receive(sock)
			#reply = sock.recv(BUFSIZE)
			print('Client received')
			print(reply)
			
        	#if reply['status'] == 200:
        		#print(GREEN + reply['message'] + END)
        		#sys.exit(0)
        	#else:
        		#print(YELLOW + reply['message'] + END)
        	#read local
"""sock = newsocket()
        	reply = transfer(filepath, sock)
        	if reply['status'] == 200:
        		print(GREEN + reply['message'] + END)
        	else:
        		print(RED + reply['message'] + END)
        	sys.exit(0)"""
        	
            



