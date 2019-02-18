include:
  - .install
  {% if grains['osmajorrelease'] == 6 %}
  - .install_openssl
  - .conf
  {% elif grains['osmajorrelease'] == 7 %}
  - .conf_centos7
  {% endif %}
