#!/bin/bash

cd /var/lib/svn/roadshow

/usr/bin/rsync -qaC --delete /var/lib/svn/roadshow/* /var/cfengine/masterfiles

cd -
