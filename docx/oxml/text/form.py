# encoding: utf-8

"""Form-related proxy types."""

from ..ns import qn
from ..xmlchemy import (
    BaseOxmlElement, ZeroOrMore, ZeroOrOne
)

class CT_Sdt(BaseOxmlElement):
    """
    ``<w:sdt>`` element, specifying form in a cell.
    """
    sdtContent = ZeroOrMore('w:sdtContent')

class CT_SdtContent(BaseOxmlElement):
    """
    ``<w:sdtContent>`` element, specifying form in a cell.
    """
    pPr = ZeroOrOne('w:pPr')
    r = ZeroOrMore('w:r')
