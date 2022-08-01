# encoding: utf-8

"""Form-related proxy types."""

from ..ns import qn
from ..xmlchemy import (
    BaseOxmlElement, ZeroOrMore, ZeroOrOne
)


class CT_Hyperlink(BaseOxmlElement):
    """
    ``<w:hyperlink>`` element, specifying hyperlink in a cell.
    """
    pPr = ZeroOrOne('w:pPr')
    r = ZeroOrMore('w:r')
