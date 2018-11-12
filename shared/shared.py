def receive(sock=None):
	if sock:
		pickled = b'' + sock.recv(BUFSIZE)
		sock.shutdown(socket.SHUT_WR)
        reply = pickle.loads(pickled)
        return reply
    else:
		pickled = sys.stdin.read()
		request = pickle.loads(pickled)
		return request
		
def send(data, sock=None):
	if sock:
		pickled = pickle.dumps(data, pickle.HIGHEST_PROTOCOL)
		pickled += b'\n'
		sock.send(pickled)
		sock.shutdown(socket.SHUT_WR)
	else:
		sys.stdout.write(pickled)
		sys.stdout.flush()
	

def checksum(path, opt):
	md5 = hashlib.md5()
	with open(path, 'rb') as f:
		content = f.read()
	md5.update(content)
	if opt == 'check':
		return md5.digest(), len(content)
	if opt == 'transfer':
		return content, md5.digest(), len(content)
	
