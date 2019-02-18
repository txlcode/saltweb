php_source:
  file.managed:
    - name: /usr/local/src/php-5.6.38.tar.gz
    - unless: test -f /usr/local/src/php-5.6.38.tar.gz
    - source: salt://php/bags/php-5.6.38.tar.gz
php_user:
  user.present:
    - name: fpm
    - createhome: False
    - gid_from_name: True
    - shell: /sbin/nologin
install_php:
  cmd.run:
    - name: cd /usr/local/src/ && tar zxf php-5.6.38.tar.gz && cd php-5.6.38/ && ./configure --prefix=/opt/php --with-mysql=mysqlnd --with-mysqli=mysqlnd --with-openssl --enable-mbstring --with-freetype-dir --with-jpeg-dir --with-png-dir --with-zlib --with-libxml-dir=/usr --enable-xml  --enable-sockets --enable-zip --enable-soap --enable-short-tags --enable-safe-mode --enable-bcmath --enable-shmop --enable-sysvsem --enable-inline-optimization  --enable-fpm --with-mcrypt  --with-config-file-path=/opt/php/etc --with-config-file-scan-dir=/opt/php/etc/php.d --with-bz2  --with-gd --enable-gd-native-ttf --enable-maintainer-zts && make && make install && mkdir -p /data/logs/php/ && chown fpm:fpm /data/logs/php -R
    - unless: test -d /opt/php/
