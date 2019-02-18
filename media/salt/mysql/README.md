修改的地方：conf/my.cnf的bind-address = {{ (grains.ip4_interfaces.eth0)[0] }}
