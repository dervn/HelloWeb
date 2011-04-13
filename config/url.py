#!/usr/bin/env python
# coding: utf-8

urls = (
    '/',        'index.Index',
    # 该行代表用户请求根目录时是去请求 index 控制器对象的 Index 方法
    '/hello',   'hello.Index',
    '/cook/*',   'cook.Index',
    '/cook/([^\x00-\xff]+)/*',   'cook.List',
    '/cook/view/(\d+)/*',   'cook.View',  
)
