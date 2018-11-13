#!/usr/bin/python2.7
#
# server_xinetd_put
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
	

def checksum(path, opt):
	md5 = hashlib.md5()
	with open(path, 'r') as f:
		content = f.read()
	md5.update(content.encode('utf-8'))
	if opt == 'check':
		return md5.hexdigest(), len(content)
	if opt == 'transfer':
		return content, md5.hexdigest(), len(content)
	

def check(request):
	path = '/home/DataCloud/' + request['username'] + '/'
	filepath = path + request['filename']
	if os.path.exists(filepath):
		md5, filesize = checksum(filepath, 'check')
		if request['md5'] == md5 and request['filesize'] == filesize:
			reply = {'status': 200, 'message': 'File already exists.' }	#do not transfer the file
		else:
			reply = {'status': 409, 'message': 'File is either corrupted or outdated. Requested transmission...', 'md5': md5 }	# transfer
	else:
		reply = {'status': 404, 'message': 'File not found. Requested transmission...'}	# transfer

	return reply


def transfer(request):
	path = '/home/DataCloud/' + request['username'] + '/'
	filepath = path + request['filename']
	with open(filepath, 'w') as f:
		f.write(request['data'])
	md5, filesize = checksum(filepath, 'check')
	if request['md5'] == md5 and request['filesize'] == filesize:
		reply = {'status': 201, 'message':  'File is succesfully transferred.'}
	else:
		reply = {'status': 500, 'message': 'Transmission failed, retry recommended.'}
	return reply
	
if __name__ == '__main__':

	request = receive()
	if request['type'] == 'check':
		reply = check(request)
	if request['type'] == 'transfer':
		reply = check(request)
	send(reply)
	
	
	

