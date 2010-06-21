#!/usr/bin/env python
# coding: utf-8

from core.config.settings import render
from core.config.settings import mysqldb


class Index:

    def GET(self):
        return render.index()