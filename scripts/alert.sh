#!/bin/bash

echo "Alert Received"

ansible-playbook \
-i ansible/inventory \
ansible/restart_nginx.yml

echo "NGINX Restarted"