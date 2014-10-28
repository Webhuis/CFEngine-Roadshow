#!/bin/bash

cd /var/lib/svn/roadshow

/usr/bin/svn update

/usr/bin/find . -name "*.cf" -exec /var/cfengine/bin/cf-promises {} \; | grep syntax

cd -
