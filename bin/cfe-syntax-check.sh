#!/bin/bash

cd /var/lib/git/CFEngine-Roadshow

/usr/bin/git pull

/usr/bin/find . -name "*.cf" -exec /var/cfengine/bin/cf-promises {} \; | grep syntax

cd -
