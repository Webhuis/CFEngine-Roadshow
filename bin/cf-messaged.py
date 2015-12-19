#!/usr/bin/python
import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5309")

while True:
    #  Wait for next request from client
    message = socket.recv()

    with open("queue.txt", "a") as queue:
      queue.write(message + "\n")

    #  Send reply back to client
    response = "message received"
    socket.send( response )

