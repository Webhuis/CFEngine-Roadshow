#!/usr/bin/python

import sys
import zmq
import json

context = zmq.Context()

#  Socket to talk to server
print("Connecting to server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://data.webhuis.nl:5309")

message = ''
# sys.argv[0] is the program filename, slice it off
for element in sys.argv[1:]:
  message = message + element

print("Sending request %s ..." % message )
socket.send( message )

#  Get the reply.
response = socket.recv()
print( response )
