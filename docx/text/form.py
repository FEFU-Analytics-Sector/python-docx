# encoding: utf-8

"""
Form-related proxy objects for python-docx, Run in particular.
"""

from __future__ import absolute_import, print_function, unicode_literals

from .run import Run
from ..shared import Parented


class Form(Parented):
    """
    Proxy object wrapping ``<w:sdt>`` element.
    """
    def __init__(self, sdt, parent):
        super(Form, self).__init__(parent)
        self._sdt = self.element = sdt

    @property
    def content(self):
        return [_FormContent(content) for content in self._sdt.sdtContent_lst]

    @property
    def text(self):
        """
        String formed by concatenating the text equivalent of each run
        content child element into a Python string.
        """
        return '\n'.join(p.text for p in self.content)


class _FormContent(object):
    """
    Proxy object wrapping ``<w:sdtContent>`` element.
    """
    def __init__(self, sdt_content):
        super(_FormContent, self).__init__()
        self._sdt_content = sdt_content

    @property
    def runs(self):
        """
        Sequence of |Run| instances corresponding to the <w:r> elements in
        this sdt.
        """
        return [Run(r, self) for r in self._sdt_content.r_lst]

    @property
    def text(self):
        text = ''
        for run in self.runs:
            text += run.text
        return text
