#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb
import os,sys
reload(sys)
sys.setdefaultencoding('utf8')
import logging
import threading
import datetime
name=sys.argv[1]
order=sys.argv[2]
lujin="cd /data/projects/cdsb_app/%s;" %(name)

class myThread (threading.Thread):
    def __init__(self, threadID, i,lujin,order):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.i = i
        self.lujin=lujin
        self.order=order
    def run(self):
        print ("开启线程：" + str(self.threadID))
        zhixing(self.i,self.lujin,self.order)
        print ("退出线程：" + self.threadID)

def get_ip_list():
    ip_list=[]
    name_list=[]
    db = MySQLdb.connect("", "githook", "", "server_machine", charset='utf8' )
    cursor = db.cursor()
    sql = "SELECT * FROM server WHERE name like '%红星新闻%';"
    #sql = "SELECT * FROM server WHERE name like '%红星新闻APP11%';"
    try:
       cursor.execute(sql)
       results = cursor.fetchall()
       for row in results:
          name=row[1]
          name_list.append(name)
          in_ip = row[3]
          ip_list.append(in_ip)
    except:
       print "Error: unable to fecth data"
    db.close()
    return name_list,ip_list
def zhixing(i,lujin,order):
    command = "ssh -o ConnectTimeout=3 cdsbxmt@%s '%s %s'" % (ip_list[i], lujin, order)
    ret = os.popen(command).read()
    print ("%s  %s  %s \n" % (name_list[i], datetime.datetime.now(), ret))
(name_list,ip_list)=get_ip_list()
nloops = range(len(ip_list))
threads = []
threadID = 1
for i in nloops:
    thread = myThread(threadID, i,lujin,order)
    thread.start()
    threads.append(thread)
    threadID += 1
for t in threads:
    t.join()
print ("退出主线程")



