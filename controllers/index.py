#!/usr/bin/env python
# coding: utf-8

from settings import render
from settings import db


class Index:

    def GET(self):
        entries = db.select('table1')
        ret = '<table>'
        if entries:        
                for entry in entries:
                        ret += '<tr><td>'+ str(entry['id'])+'</td>'+entry['name']+'</tr>'  
        ret += '</table>'              
        return render.index()
        # 请求 index 模板，可以按目录结构来写
        # 如 rendr.default.index()，代表请求 default 目录下的 index 模板
        # 模板的扩展名有要求，.html 或者 .xml 都可以