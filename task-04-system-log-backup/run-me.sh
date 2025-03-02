#!/bin/bash 
# execution wrapper that runs task #4

# backups localhost directories
ansible-playbook -i inventory.ini playbook-creates-tar.yaml -K

# transferes backup tar file to remote server
ansible-playbook -i inventory.ini playbook-send-to-server.yaml -K