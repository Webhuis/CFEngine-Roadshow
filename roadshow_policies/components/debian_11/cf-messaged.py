#!/usr/bin/env python3

import json
import zmq
import subprocess as sp
from threading import Thread   # currentThread is not used
import multiprocessing as mp
import loguru as log
import os
#import pymysql as pm
import queue as q
import time as t
import datetime as dt
import sys

#import classes_data as D

pool = mp.Pool(processes=4)
queue_manager = mp.Manager()
queues = queue_manager.Queue()

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://10.68.171.111:5309")

log.logger.add('/var/log/Data_error.log', filter = lambda record: 'error' in record['extra'] )
error_log = log.logger.bind(error = True)
log.logger.add('/var/log/Data.log', filter = lambda record: 'data' in record['extra'] )
data_log = log.logger.bind(data = True)
log.logger.add('/var/log/Data_messages.log', filter = lambda record: 'messages' in record['extra'] )
data_messages_log = log.logger.bind(data = True)

date_time = str(dt.datetime.now())

error_log.info(date_time)
data_log.info('Start run Data')
data_messages_log.info('Start run messaging')

while True:
  try:
    b_message = socket.recv()
    message = b_message.decode()
    data_messages_log.info('Receiving {}.'.format(message))
    received = True
  except Exception as e:
    data_messages_log.info('Error receiving message {}'.format(e.args))
    received = False

  if received:
    response = 'Message processed' + '\n'
    b_response = message.encode('utf8')
    try:
      socket.send_string(response)
      data_messages_log.info('Sending {}.'.format(response))
    except Exception as e:
      data_messages_log.info('Error sending message {}'.format(e.args))

socket.close()
cf_messaged_log.close()

#main()


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
