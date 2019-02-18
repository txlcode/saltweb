file_dir:
  file.recurse:
    - name: /data/projects
    - source: salt://php7/files/
    - user: root
    - file_mode: 644
    - dir_mode: 755
    - mkdir: True
    #- clean: True
