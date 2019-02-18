mysql_conf:
  file.managed:
    - name: /etc/my.cnf
    - source: salt://mysql/conf/my.cnf
    - user: root
    - group: root
    - mode: 644
