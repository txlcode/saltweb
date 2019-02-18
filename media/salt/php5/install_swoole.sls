swoole_source:
  file.managed:
    - unless: test -f /usr/local/src/swoole-1.9.20.tgz
    - name: /usr/local/src/swoole-1.9.20.tgz
    - source: salt://php/bags/swoole-1.9.20.tgz
    - user: root
    - group: root
    - mode: 644
extract_install_swoole:
  cmd.run:
    - unless: test -d /usr/local/src/swoole-1.9.20
    - cwd: /usr/local/src
    - name: tar zxvf swoole-1.9.20.tgz && cd swoole-1.9.20  &&  /opt/php/bin/phpize && ./configure --with-php-config=/opt/php/bin/php-config && make && make install && echo "extension=swoole.so" >> /opt/php/etc/php.ini 
    - require:
       - file: swoole_source
