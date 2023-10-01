#!/usr/bin/env python3

import sys
import zmq as zmq

cf_message_log = open('/var/log/cf_message_log', 'a+')

context = zmq.Context()

#  Socket to talk to server
#print("Connecting to server...")
socket = context.socket(zmq.REQ)
socket.setsockopt(zmq.LINGER, 0)
try:
  socket.connect("tcp://10.68.171.111:5309")
  cf_message_log.write('Socket connect is Ok!\n')
except Exception as e:
  cf_message_log.write('Fout in socket connect!\n')

message = ''
# sys.argv[0] is the program filename, slice it off
for element in sys.argv[1:]:
  message = message + element

#print("Sending request %s ..." % message )
try:
  socket.send( message )
  cf_message_log.write(message + '\n' + 'Query is Ok!\n')
except Exception as e:
  cf_message_log.write(message + '\n' + 'Fout in execute query!\n')

poller = zmq.Poller()
try:
  poller.register(socket, zmq.POLLIN)
  cf_message_log.write(response + '\n' + 'Query is Ok!\n')
except Exception as e:
  cf_message_log.write('Fout in execute query!' + e.args + '\n')

if poller.poll(2*1000): # 10s timeout in milliseconds
  response = socket.recv()
else:
# raise IOError("Timeout processing auth request")
  response = ("Timeout processing auth request")
# quit()

cf_message_log.write( response )
cf_message_log.close()

