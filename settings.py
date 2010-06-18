#!/usr/bin/env python
# coding: utf-8

import web


render = web.template.render('templates/', cache=False) # 设置模板目录和模板缓存
web.template.Template.globals['static'] = '/static' # 在模板中可以使用 static 该全局对象