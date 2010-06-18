#!/usr/bin/env python
# coding: utf-8

from settings import render


class Index:

    def GET(self):
        return render.index()
        # 请求 index 模板，可以按目录结构来写
        # 如 rendr.default.index()，代表请求 default 目录下的 index 模板
        # 模板的扩展名有要求，.html 或者 .xml 都可以