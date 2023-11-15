#!/usr/bin/env python3

import sys
import zmq as zmq

def message_Data(message):
  try:
    socket.connect("tcp://10.68.171.111:5309")
    socket.setsockopt(zmq.LINGER, 0)
    cf_message_log.write('Socket connect is Ok!\n')
  except Exception as e:
    cf_message_log.write('Error in socket connect!\n{}'.format(e.args))
    response = ('Error in socket connect!\n{}'.format(e.args))

  poller = zmq.Poller()
  poller.register(socket, zmq.POLLIN)
  b_message = message[0].encode('utf-8')
  cf_message_log.write('b_message in\n{}'.format(b_message))
  try:
    socket.send( b_message )
    cf_message_log.write('Message sent!\n')
  except Exception as e:
    cf_message_log.write('Error in socket send!\n{} '.format(e.args))
    response = ('Error in socket send!\n{}'.format(e.args))

  try:
    b_response = socket.recv()
    response = b_response.decode()
    cf_message_log.write(response + '\n' + 'Response is Ok!\n')
  except Exception as e:
    cf_message_log.write(message + '\n' + 'Error in response!! '.format(e.args))
    response = ('Error in response!\n{}'.format(e.args))

  cf_message_log.write(response + '\n' + 'Inhoud response voor return!\n')

  return response

cf_message_log = open('/var/log/cf_message_log', 'a+')

context = zmq.Context()
socket = context.socket(zmq.REQ)

message = sys.argv[1:]
cf_message_log.write('Message in\n{}'.format(message))
#print('message-in', message)

response = message_Data(message)
cf_message_log.write(response + '\n' + 'Inhoud response na function call.\n')
cf_message_log.close()

