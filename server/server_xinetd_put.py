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


def send(reply):
	pickled = pickle.dumps(reply, pickle.HIGHEST_PROTOCOL)
	sys.stdout.buffer.write(pickled)
	sys.stdout.flush()
	

def receive():
	pickled = sys.stdin.read()
	request = pickle.loads(pickled)
	return request
	
def sendstring(reply):
	print(reply)
	
def receivestring():
	return sys.stdin.read()


def check(request):
	path = '/home/DataCloud/' + request['username'] + '/'
	if os.path.exists(path + request['filename']):
		md5, filesize = checksum(filepath)
		if request['md5'] == md5 and request['filesize'] == filesize:
			reply = {'status':200, 'message':'File already exists.' }	#do not transfer the file
		else:
			reply = {'status':409, 'message':'File is either corrupted or outdated. Requested transmission...' }	# transfer
	else:
		reply = {'status':404, 'message':'File not found. Requested transmission...'}	# transfer
	return reply
		

def transfer(request):
	print(transfer)
	filepath = '/home/DataCloud/' + request['username'] + '/' + request['filename']
	with open(filepath, 'w') as f:
		f.write(request['data'])
	md5, filesize = checksum(filepath)
	if request['md5'] == md5 and request['filesize'] == filesize:
		reply = {'status': 201, 'message': request['filename']+ ' is succesfully transferred.'}
	else:
		reply = {'status': 500, 'message': 'Transmission failed, retry recommended.'}
		
	return reply


def checksum(path):
	md5 = hashlib.md5()
	with open(path, 'r') as f:
		content = f.read()
	md5.update(content.encode())
	return md5.hexdigest(), len(content)


if __name__ == '__main__':
	#requeststring = receivestring()
	request = receive()
	#reply = check(request)
	#print(reply)
	#sendstring('World!')
	#check(request)
	reply2 = {'status':200, 'message':'File already exists.'}
	print('Reply2' + reply2)
	sys.stdout.flush()
	send(reply)
	status == 200
	#status = check(request)
	if status != 200:
		request = receive()
		reply = transfer(request) 
		send(reply)

	
		
	
