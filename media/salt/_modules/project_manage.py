# encoding:utf-8
import os
def ProjectBackup(user_id,project_path,project_name,tag=''):
    if tag =='':
        bkpath = '/srv/backup/user_%s/project/%s/%s' % (user_id,project_name,project_path)
    else:
        bkpath = '/srv/backup/user_%s/project/%s/history/%s/%s' % (user_id, project_name, tag,project_path)
    if not os.path.isdir(os.path.dirname(bkpath)):
        os.makedirs(bkpath)
    cmd = 'rsync -lapvzrtopg  %s/ %s/' %(project_path,bkpath)
    if os.system(cmd) == 0:
        return 0
    else:
        return 1
def ProjectSync(rsync_user,user_id,modules,project_path,project_name):
    cmd='rsync -avz  --progress  --password-file=/etc/rsync.password %s@10.80.239.79::%s %s' % (rsync_user,modules,project_path)
    result = ProjectBackup(user_id, project_path,project_name)
    if result==0:
        if os.system(cmd)==0:
            return 'Backup Success! Rsync Success!'
        else:
            return 'Backup Success! Rsync Faild!'
    else:
        return 'Backup Faild! Do Not StartRsync!'

def ProjectRollback(user_id,project_path,project_name,tag):
    bkpath = '/srv/backup/user_%s/project/%s/history/%s/%s' % (user_id, project_name, tag, project_path)
    cmd = 'rsync -lapvzrtopg %s/ %s/' % (bkpath,project_path)
    if os.system(cmd) == 0:
        return 'Rollback Success!'
    else:
        return 'Rollback Faild!'
def ProjectUpdate(rsync_user,user_id,modules,project_path,project_name,tag):
    cmd = 'rsync -avz  --progress  --password-file=/etc/rsync.password %s@10.80.239.79::%s %s' % (
    rsync_user, modules, project_path)
    result = ProjectBackup(user_id, project_path, project_name,tag)
    if result==0:
        if os.system(cmd)==0:
            return 'Backup Success! Update Success!'
        else:
            return 'Backup Success! Update Faild!'
    else:
        return 'Backup Faild! Do Not StartUpdate!'

def ProjectCleanBackup(user_id,project_path,project_name,tag):
    cmd = 'rm -rf /srv/backup/user_%s/project/%s/history/%s' % (user_id, project_name, tag)
    if os.system(cmd) == 0:
        return 'CleanBackup Success!'
    else:
        return 'CleanBackup Faild!'
