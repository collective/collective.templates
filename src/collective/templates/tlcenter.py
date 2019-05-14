# -*- coding: utf-8 -*-
from Acquisition import aq_inner
from plone import api
from plone.app.layout.viewlets import ViewletBase
from plone.app.multilingual.dx import directives
from plone.app.textfield import RichText
from plone.supermodel import model
from Products.CMFPlone.browser.search import quote_chars
from Products.Five import BrowserView
from Products.ZCTextIndex.ParseTree import ParseError
from collective.templates import MessageFactory as _
from zope import schema
import re
from zope.interface import Invalid
from plone.supermodel.directives import primary

MULTISPACE = u'\u3000'.encode('utf-8')
BAD_CHARS = ('?', '-', '+', '*', MULTISPACE)

checkEmail = re.compile(
    r"[a-zA-Z0-9._%-]+@([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,4}").match


def validateEmail(value):
    if not checkEmail(value):
        raise Invalid(_(u"Invalid email address"))
    return True



class ITUpCenter(model.Schema):
    """ A Templates Upload Center.
    """

    title = schema.TextLine(
        title=_(u"Name Of The Templates Center"),
    )

    description = schema.Text(
        description=_(u"Description of the Templates Center"),
    )

    product_description = schema.Text(
        description=_(u"Description of the features of templates")
    )

    product_title = schema.TextLine(
        title=_(u"Template Product Name"),
        description=_(
            u"Name of the Template product, e.g. only Templates"),
    )

    model.fieldset('categories_et_all',
                   label=u"Categories et all",
                   fields=['available_category', 'available_licenses',
                           'available_versions', 'available_platforms'])

    available_category = schema.List(title=_(u"Available Categories"),
                                     default=['Business',
                                              ],
                                     value_type=schema.TextLine())

    available_licenses = schema.List(title=_(u"Available Licenses"),
                                     default=[
                                         'GNU-GPL-v2 (GNU General Public '
                                         'License Version 2)',
                                         'GNU-GPL-v3+ (General Public License '
                                         'Version 3 and later)',
                                         'LGPL-v2.1 (GNU Lesser General '
                                         'Public License Version 2.1)',
                                         'LGPL-v3+ (GNU Lesser General Public '
                                         'License Version 3 and later)',
                                         'BSD (BSD License (revised))',
                                         'MPL-v1.1 (Mozilla Public License '
                                         'Version 1.1)',
                                         'MPL-v2.0+ (Mozilla Public License '
                                         'Version 2.0 or later)',
                                         'CC-by-sa-v3 (Creative Commons '
                                         'Attribution-ShareAlike 3.0)',
                                         'CC-BY-SA-v4 (Creative Commons '
                                         'Attribution-ShareAlike 4.0 '
                                         'International)',
                                         'AL-v2 (Apache License Version 2.0)',
                                         ],
                                     value_type=schema.TextLine())

    available_versions = schema.List(title=_(u"Available Versions"),
                                     default=['Product 1.0',
                                     ],
                                     value_type=schema.TextLine())

    available_platforms = schema.List(title=_(u"Available Platforms"),
                                      default=['All platforms',
                                               'Linux',
                                               'Linux-x64',
                                               'Mac OS X',
                                               'Windows',
                                               'BSD',
                                               'UNIX (other)'],
                                      value_type=schema.TextLine())

    model.fieldset('instructions',
                   label=u'Instructions',
                   fields=['install_instructions', 'reporting_bugs', ])

    primary('install_instructions')
    install_instructions = RichText(
        title=_(u"Template Installation Instructions"),
        description=_(u"Please fill in the install instructions"),
        required=False
    )

    primary('reporting_bugs')
    reporting_bugs = RichText(
        title=_(u"Instruction how to report Bugs"),
        required=False
    )

    model.fieldset('disclaimer',
                   label=u'Legal Disclaimer',
                   fields=['title_legaldisclaimer', 'legal_disclaimer',
                           'title_legaldownloaddisclaimer',
                           'legal_downloaddisclaimer'])

    title_legaldisclaimer = schema.TextLine(
        title=_(u"Title for Legal Disclaimer and Limitations"),
        default=_(u"Legal Disclaimer and Limitations"),
        required=False
    )

    legal_disclaimer = schema.Text(
        title=_(u"Text of the Legal Disclaimer and Limitations"),
        description=_(
            u"Enter the text of the legal disclaimer and limitations that "
            u"should be displayed to the project creator and should be "
            u"accepted by the owner of the project."),
        default=_(
            u"Fill in the legal disclaimer, that had to be accepted by the "
            u"project owner"),
        required=False
    )

    title_legaldownloaddisclaimer = schema.TextLine(
        title=_(
            u"Title of the Legal Disclaimer and Limitations for Downloads"),
        default=_(u"Legal Disclaimer And Limitations For Downloads"),
        required=False
    )

    primary('legal_downloaddisclaimer')
    legal_downloaddisclaimer = RichText(
        title=_(u"Text of the Legal Disclaimer and Limitations for Downlaods"),
        description=_(
            u"Enter any legal disclaimer and limitations for downloads that "
            u"should appear on each page for dowloadable files."),
        default=_(u"Fill in the text for the legal download disclaimer"),
        required=False
    )

    primary('information_oldversions')
    information_oldversions = RichText(
        title=_(u"Information About Search For Old Product Versions"),
        description=_(u"Enter an information about the search for older "
                      u"versions of the product, if they are not on the "
                      u"versions list (compatibility) anymore."),
        required=False
    )

    model.fieldset('contactadresses',
                   label=u'Special Email Adresses',
                   fields=['contactForCenter'])

    contactForCenter = schema.ASCIILine(
        title=_(
            u"EMail address for communication with the template center "
            u"manager and reviewer"),
        description=_(
            u"Enter an email address for the communication with template "
            u"center manager and reviewer"),
        default='projects@foo.org',
        constraint=validateEmail
    )


directives.languageindependent('available_category')
directives.languageindependent('available_licenses')
directives.languageindependent('available_versions')
directives.languageindependent('available_platforms')
