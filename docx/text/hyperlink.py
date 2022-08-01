# encoding: utf-8

"""
Form-related proxy objects for python-docx, Run in particular.
"""

from __future__ import absolute_import, print_function, unicode_literals

from .run import Run
from ..shared import Parented


class Hyperlink(Parented):
    """
    Proxy object wrapping ``<w:hyperlink>`` element.
    """
    def __init__(self, hyperlink, parent):
        super(Hyperlink, self).__init__(parent)
        self._hyperlink = self.element = hyperlink

    @property
    def runs(self):
        """
        Sequence of |Run| instances corresponding to the <w:r> elements in
        this sdt.
        """
        return [Run(r, self) for r in self._hyperlink.r_lst]

    @property
    def text(self):
        text = ''
        for run in self.runs:
            text += run.text
        return text
