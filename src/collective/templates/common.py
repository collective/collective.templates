# -*- coding: utf-8 -*-
from collective.templates import _
from Products.CMFPlone.utils import safe_unicode
from zope.interface import Invalid
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary

import re


yesnochoice = SimpleVocabulary(
    [SimpleTerm(value=0, title=_(safe_unicode('No'))),
     SimpleTerm(value=1, title=_(safe_unicode('Yes')))],
)

checkemail = re.compile(
    r'[a-zA-Z0-9._%-]+@([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,4}').match


def validateemail(value):
    if not checkemail(value):
        raise Invalid(_(u'Invalid email address'))
    return True
