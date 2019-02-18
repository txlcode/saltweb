修改的地方
  1，文件conf/zabbix_agentd.j2的Hostname=mysql_{{ (grains.ip4_interfaces.eth1)[0] }} 
