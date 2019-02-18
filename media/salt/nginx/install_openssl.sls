openssl_source:
  file.managed:
    - unless: test -f /usr/local/src/openssl-1.1.0g.tar.gz
    - name: /usr/local/src/openssl-1.1.0g.tar.gz
    - source: salt://nginx/bags/openssl-1.1.0g.tar.gz
    - user: root
    - group: root
    - mode: 644
extract_install_nginx:
  cmd.run:
    - unless: test -d /usr/local/src/openssl-1.1.0g
    - cwd: /usr/local/src
    - names :
      - tar zxvf openssl-1.1.0g.tar.gz && cd openssl-1.1.0g && ./config --prefix=/usr/local/openssl && make && make install; mv /usr/bin/openssl  /usr/bin/openssl.old ; mv /usr/include/openssl /usr/include/openssl.old ; ln -s /usr/local/openssl/bin/openssl /usr/bin/openssl && ln -s /usr/local/openssl/include/openssl /usr/include/openssl && ln -s /usr/local/openssl/lib/libssl.so /usr/local/lib64/libssl.so && ln -s /usr/local/openssl/lib/libcrypto.so /usr/local/lib64/libcrypto.so && echo '/usr/local/openssl/lib' >> /etc/ld.so.conf
    - require:
      - file: openssl_source
      - pkg: install_soft
