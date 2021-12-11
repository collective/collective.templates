# -*- coding: utf-8 -*-
from collective.templates import _
from plone import api
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


def allowedtemplatefileextensions():
    return api.portal.get_registry_record(
        'collectivetemplates.allowed_templatefileextension').replace('|', ', ')


def allowedtempimageextensions():
    return api.portal.get_registry_record(
        'collectivetemplates.allowed_tempimageextension').replace('|', ', ')


def validatetemplatefileextension(value):
    result = str(api.portal.get_registry_record(
        'collectivetemplates.allowed_templatefileextension'))
    pattern = r'^.*\.({0})'.format(result)
    matches = re.compile(pattern, re.IGNORECASE).match
    if not matches(value.filename):
        raise Invalid(safe_unicode(
            'You could only upload files with an allowed file extension. '
            'Please try again to upload a file with the correct file'
            'extension.'))
    return True


def validateimagefileextension(value):
    result = str(api.portal.get_registry_record(
        'collectivetemplates.allowed_tempimageextension'))
    pattern = r'^.*\.({0})'.format(result)
    matches = re.compile(pattern, re.IGNORECASE).match
    if not matches(value.filename):
        raise Invalid(safe_unicode(
            'You could only upload files with an allowed file extension. '
            'Please try again to upload a file with the correct file'
            'extension.'))
    return True


def legaldeclarationtitle():
    return api.portal.get_registry_record(
        'collectivetemplates.title_legaldisclaimer')


def legaldeclarationtext():
    return api.portal.get_registry_record(
        'collectivetemplates.legal_disclaimer')
