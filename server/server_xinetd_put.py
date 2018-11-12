#!/usr/bin/python2.7
#
# server_xinetd_put
# DataMover
#
# Created by Nehir Poyraz on 11.11.2018

from shared import shared
import os
import time
import sys
import hashlib
import pickle

# already exists = 200 (OK)
# created = 201	 (CREATED)
# corrputed = 409 	(CONFLICT) 
# not found = 404  (NOTFOUND)


def env(request):
global client
global path
global filepath




def check(request):
	path = '/home/DataCloud/' + request['username'] + '/'
	if os.path.exists(path + request['filename']):
		md5, filesize = shared.checksum(filepath, 'check')
		if request['md5'] == md5 and request['filesize'] == filesize:
			reply = {'status':200, 'message':'File already exists.' }	#do not transfer the file
		else:
			reply = {'status':409, 'message':'File is either corrupted or outdated. Requested transmission...' }	# transfer
	else:
		reply = {'status':404, 'message':'File not found. Requested transmission...'}	# transfer
	
	shared.send(reply)
	return reply
		

def transfer(request):
	filepath = '/home/DataCloud/' + request['username'] + '/' + request['filename']
	with open(filepath, 'wb') as f:
		f.write(request['data'])
	md5, filesize = shared.checksum(filepath, 'check')
	if request['md5'] == md5 and request['filesize'] == filesize:
		reply = {'status': 201, 'message': request['filename']+ ' is succesfully transferred.'}
	else:
		reply = {'status': 500, 'message': 'Transmission failed, retry recommended.'}
		
	return reply


if __name__ == '__main__':
	request = shared.receive()
	status = shared(request)
	if reply['status'] != 200:
		request = shared.receive()
		reply = transfer(request) 

	
		
	
