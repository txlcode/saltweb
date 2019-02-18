install_mysql:
  pkg.installed:
    - name: mysql
    - pkgs:
      - mysql
      - mysql-server
      - mysql-devel
