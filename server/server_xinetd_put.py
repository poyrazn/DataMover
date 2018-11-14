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
	md5.update(content.encode('utf-8'))
	return md5.hexdigest(), len(content)
	


def reply(request):
	File = '/home/DataCloud/' + request['username'] + '/' + request['filename']
	if request['type'] == 'check':
		if os.path.exists(File):
			md5, filesize = checksum(File)
			if request['md5'] == md5 and request['filesize'] == filesize:
				reply = {'status': 200, 'message': 'File already exists.' }		# do not transfer the file
			else:
				reply = {'status': 409, 'message': 'File is either corrupted or outdated. Requested transmission...'}	# transfer
		else:
			reply = {'status': 404, 'message': 'File not found. Requested transmission...'}
	
	if request['type'] == 'transfer':
		with open(File, 'wb') as f:
			f.write(request['data'])
		md5, filesize = checksum(File)
		if request['md5'] == md5 and request['filesize'] == filesize:
			reply = {'status': 200, 'message': 'File is succesfully transferred' }
		else:
			reply = {'status': 500, 'message': 'Transmission failed, retry recommended.'}
	send(reply)

	
if __name__ == '__main__':

	request = receive()
	reply(request)
	
	
	
	

