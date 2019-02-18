phpredis_source:
  file.managed:
    - unless: test -f /usr/local/src/develop
    - name: /usr/local/src/develop
    - source: salt://php/bags/develop
    - user: root
    - group: root
    - mode: 644
extract_install_phpredis:
  cmd.run:
    - unless: test -d /usr/local/src/phpredis-develop
    - cwd: /usr/local/src
    - name: unzip develop && cd phpredis-develop/  &&  /opt/php/bin/phpize && ./configure --with-php-config=/opt/php/bin/php-config && make && make install && echo "extension=redis.so" >> /opt/php/etc/php.ini
    - require:
       - file: phpredis_source
