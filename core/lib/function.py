#!/usr/bin/env python
# coding: utf-8
import urllib

def urldecode(url):
    return urllib.unquote(url.replace("\\x","%"))