#!/usr/bin/env python
# coding: utf-8

from core.config.settings import mysqldb
from core.config.settings import pagesize

def get_cuisines():
    return mysqldb.select('cp',what='cx,count(cx) as count',group='cx', order='count desc')

def get_cuisine(cx):
    return mysqldb.select('cp',what='id,cm,td,yl,zzff',where='cx=$cx', order='id desc',vars=locals())

def get_top():
    """get top """
    return mysqldb.select('cp',what='id,cm,td,yl,zzff',limit=pagesize)

def list(page):
    if not page:
        page = 1
    return mysqldb.select('cp',what='id,cm,td,yl,zzff' \
                   ,where='id<'+str(int(page)*pagesize)+' and id>'+str((int(page)-1)*pagesize) \
                   ,limit=pagesize)

def get(id):
    try:
        return mysqldb.select('cp',what='id,cm,td,yl,zzff',where='id=$id',vars=locals())[0]
    except IndexError:
        return None

def count():
    return mysqldb.select('cp',what="count(1) as count")[0].count