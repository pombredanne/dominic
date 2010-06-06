# #!/usr/bin/env python
# -*- coding: utf-8 -*-
# <dominic - python-pure implementation of CSS Selectors>
# Copyright (C) <2010>  Gabriel Falcão <gabriel@nacaolivre.org>
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

version = '0.1.0'
from xml.dom import minidom
import xpath

class CSSSelect(object):
    def __init__(self, selector):
        self.selector = selector

    @property
    def path(self):
        return "//" + self.selector

class BaseHandler(object):
    def xpath(self, path):
        finder = xpath.XPath(path)
        return map(Element, finder.find(self.document))

    def find(self, selector):
        xpather = CSSSelect(selector)
        return self.xpath(xpather.path)

    def get(self, selector):
        return self.find(selector)[0]

class Element(BaseHandler):
    def __init__(self, element):
        self.element = element
        self.attribute = self._fetch_attributes(element)

    def _fetch_attributes(self, element):
        keys = element.attributes.keys()
        return dict([(k, element.getAttribute(k)) for k in keys])

class DOM(BaseHandler):
    def __init__(self, raw):
        self.raw = raw
        self.document = minidom.parseString(raw)
