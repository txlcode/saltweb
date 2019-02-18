salt://init/files/diskinit.sh:
  cmd.script:
    - unless: test -d /data
    - env:
      - BATCH: 'yes'
