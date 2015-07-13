#!/usr/bin/env python

"""
Python class example.

"""


class Element(object):
    IND_LEVEL = "    "

    def __init__(self, name="", content=""):
        self.name = name
        self.children = [content] if content else []
        self.indent = "    "

    def append(self, new_child):
        self.children.append(new_child)

    def render(self, out_file, indent=""):
        out_file.write("{}<{}>\n".format(self.indent, self.name))

        for child in self.children:
            try:
                child.render(out_file, self.indent + Element.IND_LEVEL)
            except AttributeError:
                out_file.write(self.indent + Element.IND_LEVEL + child + "\n")

        out_file.write(self.indent + "</" + self.name + ">\n")


class Html(Element):

    def __init__(self, content=""):
        Element.__init__(self, name="html")
        self.indent = ""

    def render(self, out_file, indent=""):
        out_file.write("<!DOCTYPE html>\n")
        Element.render(self, out_file)


class Body(Element):

    def __init__(self, content=""):
        Element.__init__(self, name="body", content=content)


class P(Element):

    def __init__(self, content=""):
        Element.__init__(self, name="p", content=content)
        self.indent = "        "
