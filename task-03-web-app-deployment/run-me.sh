#!/bin/bash 
# execution wrapper that runs task #3

# installs, enables and runs Nginx service 
ansible-playbook -i inventory.ini playbook.yaml 

# checks Nginx service status
systemctl is-enabled nginx > /dev/null
if [ $? -eq 0 ] ; then 
    echo service is enabled
else
    echo something wrong with nginx service
    echo execution aborted
    exit 1
fi

# functional test of web app
curl http://127.0.0.1:80 1>/dev/null 2>&1
if [ $? -eq 0 ] ; then 
    echo web app is working
fi