#!/usr/bin/env python3

import sys
import zmq as zmq

context = zmq.Context()

#  Socket to talk to server
#print("Connecting to server...")
socket = context.socket(zmq.REQ)
socket.setsockopt(zmq.LINGER, 0)
#socket.connect("tcp://data.webhuis.nl:5309")
socket.connect("tcp://10.68.171.110:5309")

message = ''
# sys.argv[0] is the program filename, slice it off
for element in sys.argv[1:]:
  message = message + element

#print("Sending request %s ..." % message )
socket.send( message )

poller = zmq.Poller()
poller.register(socket, zmq.POLLIN)
if poller.poll(2*1000): # 10s timeout in milliseconds
  response = socket.recv()
else:
# raise IOError("Timeout processing auth request")
  response = ("Timeout processing auth request")
# quit()

print( response )
