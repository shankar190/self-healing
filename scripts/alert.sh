#!/bin/bash

echo "Alert Received"

ansible-playbook \
-i inventory \
restart_nginx.yml

echo "NGINX Restarted"
