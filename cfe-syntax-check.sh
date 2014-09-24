#!/bin/bash

cd /root/mirror.webhuis.nl/roadshow/roadshow

/usr/bin/find . -name "*.cf" -exec /var/cfengine/bin/cf-promises {} \; | grep syntax

cd -
