phpini:
  file.managed:
    - name: /opt/php/etc/php.ini
    - source: salt://php7/conf/php.ini
    - user: root
    - group: root
    - mode: 644
#为minion端提供php-fpm.conf配置文件
phpfpmconf:
  file.managed:
    - name: /opt/php/etc/php-fpm.conf
    - source: salt://php7/conf/php-fpm.j2
    - template: jinja
    - user: root
    - group: root
    - mode: 644
#为minion端提供php-fpm启动脚本
php-fpm:
  file.managed:
    - name:  /usr/lib/systemd/system/php-fpm.service
    - source: salt://php7/files/php-fpm.service
    - user: root
    - group: root
    - mode: 755
  cmd.run:  #并添加为系统服务
    - names:
      - /usr/bin/systemctl daemon-reload
      - /usr/bin/systemctl enable php-fpm
    - unless: /usr/bin/systemct is-enabled php-fpm.service
      
