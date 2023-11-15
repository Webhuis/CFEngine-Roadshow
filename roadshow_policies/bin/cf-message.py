#!/usr/bin/env python3

import sys
import zmq as zmq

def message_Data(message):
  try:
    socket.connect("tcp://10.68.171.111:5309")
    socket.setsockopt(zmq.LINGER, i000)
    cf_message_log.write('Socket connect is Ok!\n')
  except Exception as e:
    cf_message_log.write('Error in socket connect! ' + "".join(e.args) + '\n')
    response = ('Error in socket connect! ' + "".join(e.args))

  # sys.argv[0] is the program filename, slice it off
  #for element in sys.argv[1:]:
  #  message = message + element

  poller = zmq.Poller()
  poller.register(socket, zmq.POLLIN)
  b_message = message[0].encode('utf-8')
  cf_message_log.write('b_message in\n{}'.format(b_message))
  try:
    socket.send( b_message )
    cf_message_log.write('Message sent!\n')
    if poller.poll(1000):
      try:
        b_response = socket.recv()
        cf_message_log.write('Receive is Ok!\n')
        #print(b_response)
        response = b_response.decode()
        cf_message_log.write(response + '\n' + 'Response is Ok!\n')
        #print('response', response)
      except Exception as e:
        cf_message_log.write(message + '\n' + 'Error in response!! ' + "".join(e.args) + '\n')
        response = ('Error in response! ' + "".join(e.args))
    else:
      cf_message_log.write(message + '\n' + 'Timeout in send!! ')
      response = ('Error in send!')
  except Exception as e:
    cf_message_log.write('Error in socket send! ' + "".join(e.args) + '\n')
    response = ('Error in socket send! ' + "".join(e.args))
  else:
    response = ("Timeout processing auth request!\n")
  return response

cf_message_log = open('/var/log/cf_message_log', 'a+')

context = zmq.Context()
socket = context.socket(zmq.REQ)

message = sys.argv[1:]
cf_message_log.write('Message in\n{}'.format(message))
#print('message-in', message)

response = message_Data(message)
cf_message_log.close()

