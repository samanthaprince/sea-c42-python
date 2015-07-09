#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.


class Element(object):

    IND_LEVEL = "    "

    def __init__(self, name="", content=""):
        self.name = name
        self.children = [content] if content else []

    def append(self, new_child):
        self.children.append(new_child)


    def render(self, file_out, indent="    "):

        file_out.write("%s<%s>" % ())
        for child in self.children:
            if (type(child) == str):
                # Add new content string without rendering
                file_out.write(child)
            else:
                # Add new child node, by recursively rendering
                content +=

        indented_content = indent + self.content
        final_content = '<%s> %s </s>\n' % \
                        (self.name, indented_content, self.name)
        file_out.write(final_content)


class Html(Element):
    def __init__(self, content=""):
        Element.__init__(self, name="html", content="<!DOCTYPE html>\n")


class Body(Element):
    def __init__(self, content="", name=""):
        Element.__init__(self, name='body')


class P(Element):
    def __init__(self, content="", name=""):
        Element.__init__(self, name='p')

    def __str__
