#!/usr/bin/env python3

import json
import psycopg2
import datetime
import zmq

cf_messaged_log= open('/var/log/cf_messaged_log', 'a+')

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://10.68.171.111:5309")

while True:
  try:
    b_message = socket.recv()
    message = b_message.decode()
    cf_messaged_log.write( 'Receiving: ' + message + '\n')
  except Exception as e:
    cf_messaged_log.write( 'Error receiving message!\n' + "".join(e.args) + '\n')

  response = 'Message processed' + '\n'
  b_response = message.encode('utf8')
  try:
    socket.send(response)
    cf_messaged_log.write( 'Sending: ' + response + '\n')
  except Exception as e:
    cf_messaged_log.write( 'Error sending message!\n' + "".join(e.args) + '\n')

conn.close()
cf_messaged_log.close()

'''
def mnmutl( content ):
  uqhost = content["request_host"]
  domain_id = content["domain"]
  role = content["role"]
# return '{"response": "data"}'
  query = "select domain_id, service_id, uqhost from role_info order by domain_id, service_id, uqhost;"
  cur = conn.cursor()
  cur.execute(query);
  conn.commit()
  domain = ''
  close_domain = ''
  close_service = ''
  close_host = ''
  response = '{'
  rows = [x for x in cur]
  cols = [x[0] for x in cur.description]
  for row in rows:
    host = row[2]
#    for col in cols:
    if row[0] > domain:
      domain = row[0]
      service = ''
      close_service = ''
      response = response + close_domain + '"' + domain + '":{'
      close_domain = ']},'
    if row[1] > service:
      service = row[1]
      close_host = ''
      response = response + close_service + '"' + service + '":['
      close_service = '],'
      close_host = ''
    response = response + close_host + '"' + host + '"'
    close_host = ','
  response = response + ']}}'
# print "hallo, ik zend"
  socket.send(response)

def tstutl():

  query = "select id, name from role;"
  cur = conn.cursor()
  cur.execute(query);
  conn.commit()
  rows = [ x for x in cur ]
  cols = [x[0] for x in cur.description]
  response = '{"response":"tstutl","roles":[{'
  close_row = ''
  for row in rows:
    response = response + close_row + '"role":{'
    col_number = 0
    close_row = '},'
    close_element = ''
    for col in cols:
     response = response + close_element + '"' + col + '":"' +  row[col_number] + '"'
     close_element = ','
     col_number = col_number + 1
  response = response + '}}]}'

def write_message(message):
  timestamp = datetime.datetime.now()
  cur = conn.cursor()
  query = "insert into json_in (id, message_in) values ( %s, %s );"
  data = (timestamp, message)
  cur.execute(query, data);
  conn.commit()

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5309")

conn = psycopg2.connect(database="raw_messages_in", user="www-data", password="We8hu15iio", host="127.0.0.1", port="5432")

while True:
  message = socket.recv()
  message_json = json.loads(message)
# print message
  if message_json["message"] == "view":
    query = message_json["query"]
    content = message_json["content"]
    if query == "mnmutl":
      response = mnmutl( content )
    elif query == "tstutl":
      response = tstutl( content )
    else:
      response = "no_role_view"
      socket.send(response)
  elif message_json["message"] == "feed":
    write_message(message)
    response = "Message filed\n"
    socket.send(response)
  elif message_json["message"] == "write":
    write_message(message)
    response = "Message filed\n"
    socket.send(response)
  else:
    write_message(message)
    response = "This message is erroneous\n"
    socket.send(response)
conn.close()
'''
