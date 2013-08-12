# -*- coding: utf-8 -*-
#
# test_text.py
#
# Copyright (C) 2013 Steve Canny scanny@cisco.com
#
# This module is part of python-docx and is released under the MIT License:
# http://www.opensource.org/licenses/mit-license.php

"""Test suite for the docx.oxml.text module."""

from docx.oxml.text import CT_P, CT_R, CT_Text

from ..unitdata import a_p, a_t, an_r


class DescribeCT_P(object):

    def it_can_construct_a_new_p_element(self):
        p = CT_P.new()
        expected_xml = a_p().with_nsdecls().xml
        assert p.xml == expected_xml

    def it_can_add_an_r_to_itself(self):
        p = a_p().with_nsdecls().element
        # exercise -----------------
        r = p.add_r()
        # verify -------------------
        assert p.xml == a_p().with_nsdecls().with_r().xml
        assert isinstance(r, CT_R)


class DescribeCT_R(object):

    def it_can_construct_a_new_r_element(self):
        r = CT_R.new()
        assert r.xml == an_r().with_nsdecls().xml


class DescribeCT_Text(object):

    def it_can_construct_a_new_t_element(self):
        text = 'foobar'
        t = CT_Text.new(text)
        assert t.xml == a_t(text).with_nsdecls().xml