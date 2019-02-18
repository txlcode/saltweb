php_running:
  service.running:
    - name: php-fpm
    - enable: True
    - require:
      - file: phpini
      - file: phpfpmconf
    - watch:
      - file: phpini
      - file: phpfpmconf
