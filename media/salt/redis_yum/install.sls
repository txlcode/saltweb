redis-install:
  pkg.installed:
    - names:
      {% if grains['osmajorrelease'] == 6 %}
      - epel-release
      {% endif %}
      - redis
/data/redis:
  file.directory:
    - user: root
    - group: root
    - mode: 757
    - makedirs: Ture
    - recurse:
      - user
      - group
      - mode
