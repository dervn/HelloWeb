#!/usr/bin/env python
# coding: utf-8

from config.settings import * 
from models import cook
from lib.function import urldecode

class Index:
    ''' '''
    def GET(self):        
        entries = cook.get_cuisines()
        title = '菜谱首页'
        return render.cook.index(entries) 
    
class List:

    def GET(self,cx):
        if debug:
            #会在web.py内置server当前运行的控制台上面打印出来结果
            print 'cx=' + cx
            print locals()
        entries = cook.get_cuisine(cx)
        #count = cook.count()        
        return render.cook.list(entries)    
    
class View:

    def GET(self,id):
        entry = cook.get(id)
        return render.cook.view(entry)     
