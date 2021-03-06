#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# @Author: qitan
# @Email: qqing_lai@hotmail.com
# @Site: https://imaojia.com
# @File: file_bakup.py
# @Time: 18-2-2 下午1:40

import os
import shutil
import hashlib
import sys
def md5sum(fname):
    """ 计算文件的MD5值
    """
    def read_chunks(fh):
        fh.seek(0)
        chunk = fh.read(8096)
        while chunk:
            yield chunk
            chunk = fh.read(8096)
        else: #最后要将游标放回文件开头
            fh.seek(0)
    m = hashlib.md5()
    if isinstance(fname, basestring) \
            and os.path.exists(fname):
        with open(fname, "rb") as fh:
            for chunk in read_chunks(fh):
                m.update(chunk)
    #上传的文件缓存 或 已打开的文件流
    elif fname.__class__.__name__ in ["StringIO", "StringO"] \
            or isinstance(fname, file):
        for chunk in read_chunks(fname):
            m.update(chunk)
    else:
        return ""
    return m.hexdigest()

def Backup(user_id, tag, remote_path,file_name):
    bkpath='/srv/backup/user_%s/%s/%s' % (user_id, tag, remote_path)
    if not os.path.isdir(os.path.dirname(bkpath)):
        os.makedirs(bkpath)
    try:
        shutil.copyfile(remote_path+'/'+file_name, bkpath+'/'+file_name)
    except:
        return file_name+':back failed!'
    else:
        return file_name+':back success!'
    # try:
    #     md5_new = md5sum(dest)
    #     if md5_new == md5:
    #         return 1
    #     else:
    #         shutil.copyfile(dest, bkpath)
    #         return 0
    # except:
    #     return None

def Rollback(user_id, tag, remote_path,file_name):
    bkpath =os.path.join('/srv/backup/user_%s/%s/%s' % (user_id, tag, remote_path),file_name)
    try:
        shutil.copyfile(bkpath, remote_path+'/'+file_name)
    except:
        return file_name+':roll failed!'
    else:	
        return file_name+':roll success!'
if __name__ == '__main__':
    fname=sys.argv[1]
    t=md5sum(fname)
    print t
