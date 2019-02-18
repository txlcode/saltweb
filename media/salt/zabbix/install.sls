zabbix_source:
  file.managed:
    - unless: test -f /usr/local/src/zabbix.tar.gz
    - name: /usr/local/src/zabbix.tar.gz
    - source: salt://zabbix/bags/zabbix.tar.gz
    - user: root
    - group: root
    - mode: 644
extract_zabbix:
  cmd.run:
    - unless: test -d /usr/local/zabbix/
    - cwd: /usr/local/src
    - names :
      - tar zxvf zabbix.tar.gz -C /usr/local
    - require:
      - file: zabbix_source
zabbix_user:
  user.present:
    - name: zabbix
    - createhome: False
    - shell: /sbin/nologin
