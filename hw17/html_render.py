#!/usr/bin/env python

"""
Python class example.

"""


class Element(object):

    def __init__(self, name="", content=""):
        self.name = name
        self.content = content

    def append(self, new_child):
        self.content += new_child

    def render(self, file):
        file.write(self.content)
