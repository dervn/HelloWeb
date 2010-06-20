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
    render = web.template.render('templates/', cache=False)
    web.template.Template.globals = glovars

#db = web.database(dbn='mysql', user='username', pw='password', db='dbname')

db = web.database(dbn='sqlite', db='db/test.sqlite')

if debug:
    print render
    print web.template.Template.globals
    print db.select('table1')[0]
    print db.select('table1')[0]['id']
    print db.select('table1')[0]['name']
