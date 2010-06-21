#!/usr/bin/env python
# coding: utf-8

from core.config.settings import render
from core.config.settings import mysqldb


class Index:

    def GET(self):
        pageSize = 10
        entries = mysqldb.select('cp',what='id,cm,td,yl,zzff',where='id<20',order='id desc',limit=pageSize)
        return render.index(entries)        