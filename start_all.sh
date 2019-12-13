#!/bin/bash
systemctl start salt-minion
systemctl start salt-master
systemctl start salt-api
systemctl start nginx
#/usr/bin/supervisorctl start all
