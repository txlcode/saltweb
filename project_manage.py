# encoding:utf-8
import os
def ProjectBackup(user_id,project_path):
    bkpath = '/srv/backup/user_%s/project/%s' % (user_id,project_path)
    if not os.path.isdir(os.path.dirname(bkpath)):
        os.makedirs(bkpath)
    cmd = 'rsync -lapvzrtopg %s/ %s/' %(project_path,bkpath)
    if os.system(cmd) == 0:
        return 'backup success!'
    else:
        return 'backup faild!'
def ProjectSync(rsync_user,user_id,modules,project_path):
    cmd='rsync -avz --progress  --password-file=/etc/rsync.password %s@10.80.239.79::%s %s' % (rsync_user,modules,project_path)
    result=ProjectBackup(user_id,project_path)
    if os.system(cmd)==0:
        return 'rsync success! '+result
    else:
        return 'rsync faild! '+result

# def ProjectRollback():

