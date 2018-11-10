#
# server_xinetd_list
# DataMover
#
# Created by Nehir Poyraz on 10.11.2018

import os
import sys

message = 'Message is received.'
buf = sys.stdin.readline().strip()
received = ''
if len(buf):
	received += buf
print(message) # Write to the standard output.
print('Message sent is: ' + received)
sys.stdout.flush() # Flush the standard output, so the message is sent.