#!/usr/bin/python

import json
import psycopg2
import datetime
import time

def check_role(role):
  data = (role)
  query = "select role_id from role where role_id = %s"
  cur = conn.cursor()
  cur.execute(query, ( [data] ) );

  row = cur.fetchone()
  if row is None:
    role_status = "no_role"
  else:
    role_status = row[0]
  return(role_status)

def check_host(host_name, domain):
  data = (host_name, domain)
  query = "select role_id from host where uqhost = %s and domain_id = %s;"
  cur = conn.cursor()
  cur.execute(query, data);

  row = cur.fetchone()
  if row is None:
    host_role_status = "no_host"
  else:
    host_role_status = row[0]
  return(host_role_status)

def check_hard_classes(uqhost, domain_id):
  data = (uqhost, domain_id)
  query = "select uqhost from hard_classes where uqhost = %s and domain_id = %s;"
  cur = conn.cursor()
  cur.execute(query, data);

  row = cur.fetchone()
  if row is None:
    hard_classes_status = "no_hard_classes"
  else:
    hard_classes_status = row[0]
  return(hard_classes_status)

def insert_host_role ( uqhost, domain, role ):
  data = ( uqhost, domain, role )
  insert = "insert into host ( uqhost, domain_id, role_id ) values ( %s, %s, %s );"
  cur = conn.cursor()
  cur.execute(insert, data);
#  if ok ==
  promise = 8
#  else
#    promise = 1
  conn.commit()

def insert_hard_classes ( uqhost, domain, os, ostype, flavor, cpus, arch ):
  data = ( uqhost, domain, os, ostype, flavor, cpus, arch )
  insert = "insert into hard_classes ( uqhost, domain_id, os, ostype, flavor, cpus, arch ) values ( %s, %s, %s, %s, %s, %s, %s );"
  cur = conn.cursor()
  cur.execute(insert, data);
  conn.commit()

def hard_classes(content):
  hard_classes_container = json.dumps(content, indent=0)
  container = json.loads(hard_classes_container)
# print container
  for key, value in container.iteritems():
    if key == "feeding_host":
      uqhost = value
    elif key == "domain":
      domain_id = value
    elif key == "os":
      os = value
    elif key == "ostype":
      ostype = value
    elif key == "flavor":
      flavor = value
    elif key == "cpus":
      cpus = value
    elif key == "arch":
      arch = value
  host_role_status = check_host( uqhost, domain_id )
  if host_role_status == "no_host":
    promise = 1
  else:
    hard_classes_status = check_hard_classes(uqhost, domain_id)
    if hard_classes_status == "no_hard_classes":
      insert_hard_classes ( uqhost, domain_id, os, ostype, flavor, cpus, arch )
      promise = 8
    else:
      promise = 9
  return ( promise )

def role_feed(content):
  host_container = json.dumps(content, indent=0)
  container = json.loads(host_container)
# print container
  for key, value in container.iteritems():
    if key == "request_host":
      uqhost = value
    elif key == "domain":
      domain_id = value
    elif key == "role":
      role = value
  host_role_status = check_host( uqhost, domain_id )

  if host_role_status == role:
    promise = 9
  elif host_role_status == "no_host":
    role_status = check_role ( role )
    if role_status == "no_role":
      promise = 1
    else:
      insert_host_role ( uqhost, domain_id, role )
      promise = 8
  elif host_role_status != role:
    promise = 2
# promise = 0
  return ( promise )

def decompose_message(json_string):
  message = json.loads(json_string)
  message_type = message["message"]
  query = message["query"]
  content = message["content"]
  return ( message_type, query, content )

def update_message_flow ( ts_id, promise ):

  data   = ( promise, ts_id )
  update = "update json_in set message_flow = %s where id = %s;"
  cur.execute( update, data )

conn = psycopg2.connect(database="raw_messages_in", user="www-data", password="We8hu15iio", host="127.0.0.1", port="5432")

while True:
  query = "select id as ts_id, message_in, message_flow from json_in where message_flow = 0 order by id DESC;"
  cur = conn.cursor()
  cur.execute(query);
  rows = [x for x in cur]
  for row in rows:
    message_id = row[0]
    json_string = row[1]
#   print json_string
    ( message_type, query, content ) = decompose_message(json_string)
    if message_type == 'feed':
#     print "feed"
      if query == "role_feed":
        promise = role_feed ( content )
      elif query == "hard_classes":
        promise = hard_classes ( content )
      else:
        promise = 99
      update_message_flow ( message_id, promise )
  conn.commit()

  time.sleep(10)

conn.close()

####  End of program  ####
