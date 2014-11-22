#!/bin/bash

cd /var/lib/git/CFEngine-roadshow

/usr/bin/rsync -qaC --delete /var/lib/git/CFEngine-roadshow/policies/masterfiles/* /var/cfengine/masterfiles
/usr/bin/rsync -qaC --delete /var/lib/git/CFEngine-roadshow/policies/dynamic_policies/* /var/cfengine/dynamic_policies

cd -
