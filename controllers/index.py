#!/usr/bin/env python
# coding: utf-8

from config.settings import * 

class Index:

    def GET(self):
        return render.index()
