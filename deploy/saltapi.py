#!/usr/bin/env python
# coding: utf8
'''
@author: qitan
@contact: qqing_lai@hotmail.com
@file: saltapi.py
@time: 2017/3/30 15:29
@desc:
'''

import sys
import urllib2, urllib

if sys.version_info < (2, 7, 9):
    import ssl
    context = None
    ssl._create_default_https_context = ssl._create_unverified_context
else:
    import ssl
    #ssl._create_default_https_context = ssl._create_unverified_context
    context = ssl._create_unverified_context()

try:
    import json
except ImportError:
    import simplejson as json

class SaltAPI(object):
    __token_id = ''
    def __init__(self,url,username,password):
        self.__url = url.rstrip('/')
        self.__user = username
        self.__password = password

    def token_id(self):
        ''' user login and get token id '''
        params = {'eauth': 'pam', 'username': self.__user, 'password': self.__password}
        encode = urllib.urlencode(params)
        obj = urllib.unquote(encode)
        content = self.postRequest(obj,prefix='/login')
        try:
            self.__token_id = content['return'][0]['token']
        except KeyError:
            raise KeyError

    def postRequest(self,obj,prefix='/'):
        url = self.__url + prefix
        headers = {'X-Auth-Token'   : self.__token_id}
        req = urllib2.Request(url, obj, headers)
        opener = urllib2.urlopen(req, context=context)
        content = json.loads(opener.read())
        return content

    def getRequest(self,prefix='/'):
        url = self.__url + prefix
        headers = {'X-Auth-Token'   : self.__token_id}
        req = urllib2.Request(url, headers=headers)
        opener = urllib2.urlopen(req, context=context)
        content = json.loads(opener.read())
        return content

    def list_all_key(self):
        '''
        获取包括认证、未认证salt主机
        '''

        params = {'client': 'wheel', 'fun': 'key.list_all'}
        obj = urllib.urlencode(params)
        self.token_id()
        content = self.postRequest(obj)
        minions = content['return'][0]['data']['return']['minions']
        minions_pre = content['return'][0]['data']['return']['minions_pre']
        return minions,minions_pre

    def delete_key(self,node_name):
        '''
        拒绝salt主机
        '''

        params = {'client': 'wheel', 'fun': 'key.delete', 'match': node_name}
        obj = urllib.urlencode(params)
        self.token_id()
        content = self.postRequest(obj)
        ret = content['return'][0]['data']['success']
        return ret

    def accept_key(self,node_name):
        '''
        接受salt主机
        '''

        params = {'client': 'wheel', 'fun': 'key.accept', 'match': node_name}
        obj = urllib.urlencode(params)
        self.token_id()
        content = self.postRequest(obj)
        ret = content['return'][0]['data']['success']
        return ret

    def salt_runner(self,jid):
        '''
        通过jid获取执行结果
        '''

        params = {'client':'runner', 'fun':'jobs.lookup_jid', 'jid': jid}
        params = {}
        obj = urllib.urlencode(params)
        self.token_id()
        content = self.getRequest(prefix='/jobs/{}'.format(jid))
        #ret = content['info'][0]['Result']
        return content

    def salt_running_jobs(self):
        '''
        获取运行中的任务
        '''

        params = {'client':'runner', 'fun':'jobs.active'}
        obj = urllib.urlencode(params)
        self.token_id()
        content = self.postRequest(obj)
        ret = content['return'][0]
        return ret

    def remote_execution(self,tgt,fun,arg,expr_form):
        '''
        异步执行远程命令
        '''
        if arg:
            params = {'client': 'local_async', 'tgt': tgt, 'fun': fun, 'arg': arg, 'expr_form': expr_form}
        else:
            params = {'client': 'local_async', 'tgt': tgt, 'fun': fun, 'expr_form': expr_form}
        obj = urllib.urlencode(params)
        self.token_id()
        content = self.postRequest(obj)
        jid = content['return'][0]['jid']
        return jid

    def remote_module(self,tgt,fun,arg,kwarg,expr_form):
        '''
        异步部署模块
        '''

        params = {'client': 'local_async', 'tgt': tgt, 'fun': fun, 'arg': arg, 'expr_form': expr_form}
        #kwarg = {'SALTSRC': 'PET'}
        params2 = {'arg':'pillar={}'.format(kwarg)}
        arg_add = urllib.urlencode(params2)
        obj = urllib.urlencode(params)
        obj = obj + '&' + arg_add
        self.token_id()
        content = self.postRequest(obj)
        jid = content['return'][0]['jid']
        return jid
    def remote_module1(self,tgt,fun,arg,expr_form,arg1=''):
        '''
        异步部署模块
        '''
        params = {'client': 'local_async', 'tgt': tgt, 'fun': fun, 'arg': arg, 'expr_form': expr_form}
        #设置pillar
        #kwarg = {'SALTSRC': 'PET'}
        #params2 = {'arg': 'pillar={}'.format(kwarg)}
        obj = urllib.urlencode(params)
        def canshu(arg):
            params2 = {'arg':arg}
            return urllib.urlencode(params2)
        if arg1:
            obj = obj + '&' + canshu(arg1)
        self.token_id()
        content = self.postRequest(obj)
        return content
    def remote_localexec(self,tgt,fun,arg,expr_form):
        params = {'client': 'local', 'tgt': tgt, 'fun': fun, 'arg': arg, 'expr_form': expr_form}
        obj = urllib.urlencode(params)
        self.token_id()
        content = self.postRequest(obj)
        ret = content['return'][0]
        return ret
    def remote_localexec1(self,tgt,fun,arg):
        params = {'client': 'local', 'tgt': tgt, 'fun': fun, 'arg': arg}
        obj = urllib.urlencode(params)
        self.token_id()
        content = self.postRequest(obj)
        ret = content['return'][0]
        return ret

    def salt_state(self,tgt,arg,expr_form):
        '''
        sls文件
        '''
        params = {'client': 'local', 'tgt': tgt, 'fun': 'state.sls', 'arg': arg, 'expr_form': expr_form}
        obj = urllib.urlencode(params)
        self.token_id()
        content = self.postRequest(obj)
        ret = content['return'][0]
        return ret
    def get_modules_fun(self,tgt,fun):
        params = {'client': 'local', 'tgt': tgt, 'fun': fun}
        obj = urllib.urlencode(params)
        self.token_id()
        content = self.postRequest(obj)
        return content

    def project_manage(self,tgt,fun,arg1,arg2,arg3,arg4,arg5,expr_form):
        '''
        文件上传、备份到minion、项目管理
        '''
        params = {'client': 'local', 'tgt': tgt, 'fun': fun, 'arg': arg1, 'expr_form': expr_form}
        # 拼接url参数
        params2 = {'arg':arg2}
        arg_add = urllib.urlencode(params2)
        obj = urllib.urlencode(params)
        obj = obj + '&' + arg_add
        params3 = {'arg': arg3}
        arg_add = urllib.urlencode(params3)
        obj = obj + '&' + arg_add
        params4 = {'arg': arg4}
        arg_add = urllib.urlencode(params4)
        obj = obj + '&' + arg_add
        params5 = {'arg': arg5}
        arg_add = urllib.urlencode(params5)
        obj = obj + '&' + arg_add
        self.token_id()
        content = self.postRequest(obj)
        ret = content['return'][0]
        return ret

    def file_copy(self,tgt,fun,arg1,arg2,expr_form):
        '''
        文件上传、备份到minion、项目管理
        '''
        params = {'client': 'local', 'tgt': tgt, 'fun': fun, 'arg': arg1, 'expr_form': expr_form}
        # 拼接url参数
        params2 = {'arg':arg2}
        arg_add = urllib.urlencode(params2)
        obj = urllib.urlencode(params)
        obj = obj + '&' + arg_add
        self.token_id()
        content = self.postRequest(obj)
        ret = content['return'][0]
        return ret

    def file_bak(self,tgt,fun,arg,expr_form):
        '''
        文件备份到master
        '''
        params = {'client': 'local', 'tgt': tgt, 'fun': fun, 'arg': arg, 'expr_form': expr_form}
        obj = urllib.urlencode(params)
        self.token_id()
        content = self.postRequest(obj)
        ret = content['return'][0]
        return ret

    def file_manage(self,tgt,fun,arg1,arg2,arg3,expr_form):
        '''
        文件回滚
        '''
        params = {'client': 'local', 'tgt': tgt, 'fun': fun, 'arg': arg1, 'expr_form': expr_form}
        params2 = {'arg': arg2}
        arg_add = urllib.urlencode(params2)
        obj = urllib.urlencode(params)
        obj = obj + '&' + arg_add
        params3 = {'arg': arg3}
        arg_add_2 = urllib.urlencode(params3)
        obj = obj + '&' + arg_add_2
        self.token_id()
        content = self.postRequest(obj)
        ret = content['return'][0]
        return ret

    def salt_alive(self,tgt):
        '''
        salt主机存活检测
        '''

        params = {'client': 'local', 'tgt': tgt, 'fun': 'test.ping'}
        obj = urllib.urlencode(params)
        self.token_id()
        content = self.postRequest(obj)
        ret = content['return'][0]
        return ret

    def remote_server_info(self,tgt,fun):
        '''
        获取远程主机信息
        '''
        params = {'client': 'local', 'tgt': tgt, 'fun': fun}
        obj = urllib.urlencode(params)
        self.token_id()
        content = self.postRequest(obj)
        ret = content['return'][0][tgt]
        return ret

def main():
    sapi = SaltAPI(url='https://172.29.3.66:8000',username='saltapi',password='123456')
    arg='mysql,nginx'
    arg1='test=true'
    print arg
    jid1 = sapi.remote_module1('slave1', 'state.sls', arg, 'nodegroup', arg1)
    jid = jid1['return'][0]['jid']
    rst_source = sapi.salt_runner(jid)
    rst = rst_source['info'][0]['Result']
    print jid
    print rst_source
if __name__ == '__main__':
    main()

