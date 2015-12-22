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
    #  Wait for next request from client
    message = socket.recv()
    timestamp = datetime.now()
    cur = conn.cursor()
    cur.execute("insert into json_in (id, message_in) values ( timestamp, message )");
    conn.commit()
#    with open("queue.txt", "a") as queue:
#      queue.write(message + "\n")

    #  Send reply back to client
    response = "message received"
    socket.send( response )
conn.close()
