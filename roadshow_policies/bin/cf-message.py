#!/usr/bin/env python3

import sys
import zmq as zmq

cf_message_log = open('/var/log/cf_message_log', 'a+')

context = zmq.Context()

#  Socket to talk to server

socket = context.socket(zmq.REQ)

try:
  socket.connect("tcp://10.68.171.111:5309")
  cf_message_log.write('Socket connect is Ok!\n')
except Exception as e:
  cf_message_log.write('Error in socket connect! ' + "".join(e.args) + '\n')

message = ''
# sys.argv[0] is the program filename, slice it off
for element in sys.argv[1:]:
  message = message + element

b_message = bytes(message, 'utf-8')
cf_message_log.write(b_message)
try:
  socket.send( b_message )
  cf_message_log.write(message + '\n' + 'Query is Ok!\n')
except Exception as e:
  cf_message_log.write(message + '\n' + 'Error in socket send! ' + "".join(e.args) + '\n')

try:
  response = socket.recv()
except Exception as e:
  cf_message_log.write(message + '\n' + 'Error in response!! ' + "".join(e.args) + '\n')
else:
  response = ("Timeout processing auth request!\n")

cf_message_log.close()

