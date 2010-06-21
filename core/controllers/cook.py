#!/usr/bin/env python
# coding: utf-8

from core.config.settings import render
from core.config.settings import mysqldb
from webhelpers.paginate import Page

pageSize = 10
class Index:

    def GET(self):        
        entries = mysqldb.select('cp',what='id,cm,td,yl,zzff',limit=pageSize)
        from webhelpers.paginate import Page
        return render.cook.index(entries) 
    
class List:

    def GET(self,page):
        if not page:
            page = 1
        entries = mysqldb.select('cp',what='id,cm,td,yl,zzff',where='id<'+str(int(page)*pageSize)+' and id>'+str((int(page)-1)*pageSize),limit=pageSize)
        count = mysqldb.select('cp',what="count(1) as count")[0].count
        
        return render.cook.list(entries)    
    
class View:

    def GET(self,id):
        entry = mysqldb.select('cp',what='id,cm,td,yl,zzff',where='id='+id)
        return render.cook.view(entry[0])     