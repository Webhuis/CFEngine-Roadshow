#!/bin/bash

cd /var/lib/git/CFEngine-Roadshow

/usr/bin/rsync -qaC --delete /var/lib/git/CFEngine-Roadshow/policies/masterfiles/* /var/cfengine/masterfiles
/usr/bin/rsync -qaC --delete /var/lib/git/CFEngine-Roadshow/policies/dynamic_policies/* /var/cfengine/dynamic_policies

cd -
