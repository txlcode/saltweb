php_source:
  file.managed:
    - name: /usr/local/src/php-7.2.12-mian_anzhuang.tar.gz
    - unless: test -f /usr/local/src/php-7.2.12-mian_anzhuang.tar.gz
    - source: salt://php7/bags/php-7.2.12-mian_anzhuang.tar.gz
php_user:
  user.present:
    - name: fpm
    - createhome: False
    - shell: /sbin/nologin
install_php:
  cmd.run:
    - name: cd /usr/local/src/ && tar zxf php-7.2.12-mian_anzhuang.tar.gz -C /opt  && mkdir -p /data/logs/php/ && chown fpm:fpm /data/logs/php -R
    - unless: test -d /opt/php
