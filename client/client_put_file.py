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

from shared import shared
import socket
import os
import sys
import hashlib
import pickle

HOST = 'localhost'
PORT = 2222
ADDR = (HOST, PORT)
BUFSIZE = 4096

RED = '\033[91m'	# fail
GREEN = '\033[92m'	# success
LIGHTBLUE = '\033[96m'	# file already exists
YELLOW = '\033[93m'	# request sent
END = '\033[0m'		

def newsocket():
	newsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	newsocket.connect(ADDR)
	return newsocket
	
def check(path, sock):
	md5, filesize = shared.checksum(path, 'check')
	request = {'username': os.getlogin(), 'filename': sys.argv[1],'md5': md5, 'filesize': filesize}
	shared.send(request, sock)
	reply = shared.receive(sock)
	return reply

def transfer(path, sock):
	data, md5, filesize = shared.checksum(path, 'transfer')
	request = {'username': os.getlogin(), 'filename': sys.argv[1], 'data' : data , 'md5': md5, 'filesize': filesize}
	shared.send(request, sock)
	reply = shared.receive(sock)
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
			reply = check(filepath, sock)
        	if reply['status'] == 200:
        		print(GREEN + reply['message'] + END)
        		sys.exit(0)
        	else:
        		print(YELLOW + reply['message'] + END)
        	#read local
        	sock = newsocket()
        	reply = transfer(filepath, sock)
        	if reply['status'] == 200:
        		print(GREEN + reply['message'] + END)
        	else:
        		print(RED + reply['message'] + END)
        	sys.exit(0)
        	
            



