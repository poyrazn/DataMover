#!/usr/bin/python2.7
#
# server_xinetd_get
# DataMover
#
# Created by Nehir Poyraz on 11.11.2018


import os
import time
import sys
import hashlib
import pickle


# already exists = 200 (OK)
# created = 201	 (CREATED)
# corrputed = 409 	(CONFLICT) 
# not found = 404  (NOTFOUND)

global client
global path
global filepath

def receive():
	pickled = sys.stdin.read()
	request = pickle.loads(pickled)
	return request
	
def send(reply):
	reply = pickle.dumps(reply, pickle.HIGHEST_PROTOCOL)
	sys.stdout.write(reply)
	sys.stdout.flush()
	

def checksum(File):
	md5 = hashlib.md5()
	with open(File, 'r') as f:
		content = f.read()
	return content, md5.hexdigest(), len(content)


def reply(request):
	File = '/home/DataCloud/' + request['username'] + '/' + request['filename']
	if os.path.exists(File):
		data, md5, filesize = checksum(File)
		reply = {'status': 202, 'message': 'Transferring file', 'md5': md5, 'filesize': filesize , 'data' : data}
		send(reply)
	else:
		reply = {'status': 404, 'message': 'File not found.'}


if __name__ == '__main__':
	request = receive()
	reply(request)


