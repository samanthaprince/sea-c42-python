#!/usr/bin/env python

"""
Python class example.

"""


class Element(object):
    IND_LEVEL = "    "
    name = "html"

    def __init__(self, content="", **kwargs):
        self.attributes = kwargs
        self.attr = ""
        self.children = [content] if content else []
        for attr_key, attr_val in self.attributes.items():
            self.attr += "{key}=\"{val}\"".format(key=attr_key, val=attr_val)

    def append(self, new_child):
        self.children.append(new_child)

    indent = "    "

    def render(self, out_file, indent=""):
        out_file.write(self.indent + "<" + self.name + self.attr + ">\n")

        for child in self.children:
            try:
                child.render(out_file, self.indent + Element.IND_LEVEL)
            except AttributeError:
                out_file.write(self.indent + Element.IND_LEVEL + child + "\n")

        out_file.write(self.indent + "</" + self.name + ">\n")


class Html(Element):

    name = "html"

    def __init__(self, content=""):
        Element.__init__(self, name="html")
        self.indent = ""

    def render(self, out_file, indent=""):
        out_file.write("<!DOCTYPE html>\n")
        Element.render(self, out_file)


class Head(Element):

    name = "head"

    # def __init__(self, content=""):
    # Element.__init__(self, name="head")


class OneLineTag(Element):
    def render(self, out_file, content):
        out_file.write(self.indent + "<" + self.name + ">")

        for child in self.children:
            try:
                child.render(out_file, self.indent)
            except AttributeError:
                out_file.write(child)

        out_file.write("</" + self.name + ">\n")


class Title(OneLineTag):

    name = "title"

    def __init__(self, content=""):
        Element.__init__(self, name="title", content=content)


class Body(Element):

    name = "body"

    # def __init__(self, content=""):
    # Element.__init__(self, name="body", content=content)


class P(Element):

    name = "p"
    indent = "        "

    # def __init__(self, content=""):
    # Element.__init__(self, name="p", content=content)
    # self.indent = "        "


class SelfClosingTag(Element):
    def render(self, out_file, indent=""):
        out_file.write(self.indent + "<" + self.name + self.attr + "/>\n")


class Hr(SelfClosingTag):

    name = "hr"


class Br(SelfClosingTag):

    name = "br"
