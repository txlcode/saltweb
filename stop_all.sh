#!/bin/bash
systemctl stop salt-minion
systemctl stop salt-master
systemctl stop salt-api
systemctl stop nginx
#/usr/bin/supervisorctl stop all
