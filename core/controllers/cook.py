#!/usr/bin/env python
# coding: utf-8

from core.config.settings import render
from core.models import cook

class Index:
    ''' '''
    def GET(self):        
        entries = cook.get_top()
        return render.cook.index(entries) 
    
class List:

    def GET(self,page):
        entries = cook.list(page)
        count = cook.count()        
        return render.cook.list(entries)    
    
class View:

    def GET(self,id):
        entry = cook.get(id)
        return render.cook.view(entry)     