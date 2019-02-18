mysql_source:
  file.managed:
    - name: /usr/local/src/mysql-5.7.22.tar.gz
    - unless: test -f /usr/local/src/mysql-5.7.22.tar.gz
    - source: salt://mysql/bags/mysql-5.7.22.tar.gz

mysql_user:
  user.present:
    - name: mysql
   # - uid: 1024
    - createhome: True
   # - gid_from_name: True
    - shell: /sbin/nologin

extract_mysql:
  cmd.run:
    - cwd: /usr/local/src/
    - names:
       - tar zxvf mysql-5.7.22.tar.gz && mkdir -p /data/database/data/ && mkdir -p /usr/local/boost/ && mkdir -p /data/database/mysql-binlog && /bin/chown -R mysql:mysql /data/database/
    - unless: test -d /usr/local/src/mysql-5.7.22/
    - require:
       - file: mysql_source
#instsll_boost:
#  cmd.run:
#    - cwd: /usr/local/src
#    - names:
#       - tar -xzvf boost_1_59_0.tar.gz && cd boost_1_59_0 && ./bootstrap.sh --with-libraries=system,filesystem,log,thread --with-toolset=gcc && ./b2 toolset=gcc && ./b2 install --prefix=/usr/local/boost
#    - unless: test -d /usr/local/boost/
boost_source:
  file.managed:
    - name: /usr/local/boost/boost_1_59_0.tar.gz
    - unless: test -f /usr/local/boost/boost_1_59_0.tar.gz
    - source: salt://mysql/bags/boost_1_59_0.tar.gz
    - require:
      - cmd: extract_mysql
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
    - cwd: /usr/local/src/mysql-5.7.22/
    - names:
      - cmake -DCMAKE_INSTALL_PREFIX=/opt/mysql -DMYSQL_DATADIR=/data/database/data -DSYSCONFDIR=/etc -DWITH_MYISAM_STORAGE_ENGINE=1 -DWITH_INNOBASE_STORAGE_ENGINE=1 -DWITH_MEMORY_STORAGE_ENGINE=1 -DWITH_READLINE=1 -DMYSQL_UNIX_ADDR=/tmp/mysqld.sock -DMYSQL_TCP_PORT=3306 -DENABLED_LOCAL_INFILE=1 -DWITH_PARTITION_STORAGE_ENGINE=1 -DEXTRA_CHARSETS=all -DDEFAULT_CHARSET=utf8 -DDEFAULT_COLLATION=utf8_general_ci -DWITH_BOOST=/usr/local/boost && make && make install
    - require:
      - file: boost_source
      - cmd: extract_mysql
      - pkg: mysql_pkg
    - unless: test -d /opt/mysql/
