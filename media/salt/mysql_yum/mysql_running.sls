mysql_running:
  service.running:
    - name: mysqld
    - enable: True
    - require:
      - pkg: install_mysql
    - watch:
      - file: mysql_conf
