phpredis_source:
  file.managed:
    - unless: test -f /usr/local/src/phpredis-2.2.4.tar.gz
    - name: /usr/local/src/phpredis-2.2.4.tar.gz
    - source: salt://php/bags/phpredis-2.2.4.tar.gz
    - user: root
    - group: root
    - mode: 644
extract_install_phpredis:
  cmd.run:
    - unless: test -d /usr/local/src/phpredis-2.2.4
    - cwd: /usr/local/src
    - name: tar zxvf phpredis-2.2.4.tar.gz && cd phpredis-2.2.4/  &&  /opt/php/bin/phpize && ./configure --with-php-config=/opt/php/bin/php-config && make && make install && "extension=redis.so" >> /opt/php/etc/php.ini 
    - require:
       - file: phpredis_source
