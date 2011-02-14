#!/usr/bin/env python
# coding: utf-8

import web

debug = True
web.config.debug = debug
web.webapi.internalerror = web.debugerror

#mako
template = ''
#that can using in templates of golbal vars
glovars = {
    'static':'/static'
    }
    
if template == 'mako':
    from web.contrib.template import render_mako
    render = render_mako(directories=['templates'],input_encoding='utf-8',output_encoding='utf-8')
else:
    #setting template and cache directory 
    render = web.template.render('templates/',base='base',cache=False)
    web.template.Template.globals = glovars

#mysql 
mysqldb = web.database(dbn='mysql', user='root', pw='', db='cook',\
                       host='localhost',port=3306,charset='utf8',use_unicode=False)
#sqlite
db = web.database(dbn='sqlite', db='db/test.sqlite')

#per_page
pagesize = 10

if debug:
    print render
    print web.template.Template.globals
    print db.select('table1')[0]
    print db.select('table1')[0]['id']
    print db.select('table1')[0]['name']
