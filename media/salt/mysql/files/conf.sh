#!/bin/bash
if [  -f '/opt/mysql/scripts/mysql_install_db' ];then
	/opt/mysql/scripts/mysql_install_db --defaults-file=/etc/my.cnf --user=mysql --basedir=/opt/mysql/ --datadir=/data/database/data
elif [  -f '/opt/mysql/bin/mysql_install_db' ];then
	/opt/mysql/bin/mysql_install_db --defaults-file=/etc/my.cnf --user=mysql --basedir=/opt/mysql/ --datadir=/data/database/data
fi
