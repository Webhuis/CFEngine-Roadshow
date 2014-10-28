#!/bin/bash

cd /var/lib/svn/roadshow

/usr/bin/rsync -qaC --delete /var/lib/svn/roadshow/masterfiles/* /var/cfengine/masterfiles
/usr/bin/rsync -qaC --delete /var/lib/svn/roadshow/dynamic_policies/* /var/cfengine/dynamic_policies

cd -
