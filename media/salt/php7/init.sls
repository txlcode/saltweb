include:
  - .install_soft
  {% if grains['osmajorrelease'] == 6 %}
  - .install_php7
  - .conf
  {% elif grains['osmajorrelease'] == 7 %}
  - .install_php7_centos7
  - .conf_centos7
  {% endif %}
  - .install_php7redis
  - .install_swoole
  - .php_running
