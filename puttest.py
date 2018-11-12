def setup():
	print('Setup start')
	pickled = sys.stdin.read()
    request = pickle.loads(pickled)
    cpath = '/home/DataCloud/' + request['client'] + '/'
    cfilename = request['filename']
    cfilepath = cpath + cfilename
    cmd5 = request['md5']
    cfilesize = request['filesize']
    print("Setup complete")
    

def check(path):
	if os.path.exists(path):
		print('exists')
    	f = open(path)
    	content = f.read()
    	f.close()
    	fsize = os.path.getsize(path)
    	if md5(path) == cmd5:
    		if fsize == cfilesize:
    			reply = {
    				'status': 200
    				'message': 'OK'
    			}
    			print('200')
    		else:
				reply = {
					'status': 503
					'message': '\033[91mFile is either corrupted or outdated.\033[0m'
				}
				print('503')
    		
		else:
			reply = {
				'status': 503
				'message': '\033[91mFile is either corrupted or outdated.\033[0m'
			}
			print('503') 			
	else:
		reply = {
			'status': 404
			'message': '\033[94m' + cfilename + ' is being stored...'
		}
		print('404')
	#pickled = pickle.dumps(reply, pickle.HIGHEST_PROTOCOL)
	#pickled = b''+pickled
	#sys.stdout.write(pickled)
	sys.stdout.flush()
	return
		
def md5(path):
	md5 = hashlib.md5()
	f = open(filename)
	content = f.read()
	f.close()
	md5.update(content.encode('utf-8'))
	return md5.digest()

if __name__ == '__main__':
	print("What")
	sys.stdout.flush()
	setup()
	#print(cfilepath)
	#check(cfilepath)



    """md5 = hashlib.md5()
    pickled = sys.stdin.read()
    data = pickle.loads(pickled)
    path = '/home/DataCloud/' + data['client'] + '/'
    filename = data['filename']
    filepath = path +  filename
    if os.path.exists(filepath):
    	f = open(filepath)
    	content = f.read()
    	filesize = os.path.getsize(filepath)
    	md5.update(content.encode('utf-8'))
    	checksum = md5.digest()
    	if data['md5'] == checksum:
    		#print('File exists, checksum match.')
    		if data['filesize'] == filesize:
    			#current = ['Current']
    			#print(current)
    			print('Current implementation, subject to change.')"""
    			"""check_reply = {
        		'status': 200,
        		'message': 'Success'
        		'log': 'Success'
        		}
				print(reply['status'])
				pickled = pickle.dumps(reply, pickle.HIGHEST_PROTOCOL)
				sys.stdout.write(pickled)
				sys.stdout.flush()
    	else:
    		print('\033[91mFile is either corrupted or outdated.\033[0m')
    else:
    	print('\033[94m' + filename + ' is being stored...')
    	for i in range(80):
            print ('=', end='')
        f = open(filepath, 'w')
        f.write(data['content'])
        f.close()
        f = open(filepath)
        content = f.read()
        print('  100 % Complete!\033[0m')"""
        

		
    """if os.path.exists(filepath):
        with open(filepath) as f:
            md5.update(f.read().encode('utf-8'))
        print('\033[93mFile' + filename + ' exists. Calculating MD5 checksum.\033[0m', flush=True)
        if clientmd5 == md5.digest():
            print('\033[92mFile ' + filename + ' is succesfully recorded. MD5 checksum passed.\033[0m', flush=True)
        else:
            print('\033[91mFile is either corrupted, interrupted or outdated.\033[0m', flush=True)

    else:
        print('\033[94m' + filename + ' is being stored...', flush=True)
        starttime = time.ctime()
        f = open(filepath, 'w')
        endtime = time.ctime()
        for i in range(100):
            print ('=', end='', flush=True)
        print('100 % Complete! (', endtime-starttime, 'secs )\033[0m', flush=True)
        f.write(content)
        f.close()
        with open(filepath) as f:
            md5.update(f.read())
        if clientmd5 == md5.digest():
            print('\033[92mFile ' + filename + ' is succesfully recorded. MD5 checksum passed.\033[0m', flush=True)
        else:
            print('\033[91mTransmission failed. Retry recommended.\033[0m', flush=True)"""
