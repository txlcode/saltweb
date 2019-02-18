redis-install:
  pkg.installed:
    - name: redis
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
