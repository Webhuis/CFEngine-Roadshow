#!/usr/bin/python

import json
import psycopg2
import datetime
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5309")

conn = psycopg2.connect(database="raw_messages_in", user="www-data", password="We8hu15iio", host="127.0.0.1", port="5432")

while True:
    message = socket.recv()
    timestamp = datetime.datetime.now()
    cur = conn.cursor()
    query = "insert into json_in (id, message_in) values ( %s, %s );"
    data = (timestamp, message)
    cur.execute(query, data);
    conn.commit()
    response = "message received"
    socket.send( response )
conn.close()
