#!/bin/bash

policy_dir=/var/lib/git/CFEngine-Roadshow
policy_hub=`hostname -f`

echo ${policy_hub}

cd ${policy_dir}

git pull

/etc/init.d/cfengine3 stop

rm -rf /var/cfengine/masterfiles/*
rm -rf /var/cfengine/inputs/*
rm -rf /var/cfengine/roadshow_data
rm -rf /var/cfengine/roadshow_policies

cp -a ${policy_dir}/masterfiles/3_7_5/* /var/cfengine/masterfiles
cp -a ${policy_dir}/masterfiles_updates/3_7_5/* /var/cfengine/masterfiles

cp -a ${policy_dir}/roadshow_data /var/cfengine
cp -a ${policy_dir}/roadshow_policies /var/cfengine

rm /var/cfengine/masterfiles/cf_promises_validated
rm /var/cfengine/masterfiles/services/autorun/hello.cf

find /var/cfengine/masterfiles -type f -exec chmod -R 600 {} \;
find /var/cfengine/roadshow_policies -type f -exec chmod -R 600 {} \;
chmod +x /var/cfengine/roadshow_policies/bin/*.py

cf-agent -B ${policy_hub}
