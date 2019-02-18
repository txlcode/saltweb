mysql_source:
  file.managed:
    - name: /usr/local/src/mysql-5.6.30.tar.gz
    - unless: test -f /usr/local/src/mysql-5.6.30.tar.gz
    - source: salt://mysql/bags/mysql-5.6.30.tar.gz

mysql_user:
  user.present:
    - name: mysql
    - uid: 1024
    - createhome: True
#    - gid_from_name: True
    - shell: /sbin/nologin

extract_mysql:
  cmd.run:
    - cwd: /usr/local/src/
    - names:
       - tar zxvf mysql-5.6.30.tar.gz && mkdir -p /data/database/data/ && mkdir -p /data/database/mysql-binlog && /bin/chown -R mysql:mysql /data/database/
    - unless: test -d /usr/local/src/mysql-5.6.30
    - require:
       - file: mysql_source

mysql_pkg:
  pkg.installed:
    - pkgs:
      - gcc
      - gcc-c++
      - autoconf
      - automake
      - openssl
      - openssl-devel
      - zlib
      - zlib-devel
      - ncurses-devel
      - libtool-ltdl-devel
      - cmake

mysql_commpile:
  cmd.run:
    - cwd: /usr/local/src/mysql-5.6.30/
    - names:
      - cmake -DCMAKE_INSTALL_PREFIX=/opt/mysql -DMYSQL_DATADIR=/data/database/data -DSYSCONFDIR=/etc -DWITH_MYISAM_STORAGE_ENGINE=1 -DWITH_INNOBASE_STORAGE_ENGINE=1 -DWITH_MEMORY_STORAGE_ENGINE=1 -DWITH_READLINE=1 -DMYSQL_UNIX_ADDR=/tmp/mysqld.sock -DMYSQL_TCP_PORT=3306 -DENABLED_LOCAL_INFILE=1 -DWITH_PARTITION_STORAGE_ENGINE=1 -DEXTRA_CHARSETS=all -DDEFAULT_CHARSET=utf8 -DDEFAULT_COLLATION=utf8_general_ci && make && make install
    - require:
      - cmd: extract_mysql
      - pkg: mysql_pkg
    - unless: test -d /opt/mysql/
