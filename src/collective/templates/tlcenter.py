# -*- coding: utf-8 -*-
from Acquisition import aq_inner
from collective.templates import _
from plone import api
from plone.app.layout.viewlets import ViewletBase
from plone.app.multilingual.dx import directives
from plone.app.textfield import RichText
from plone.supermodel import model
from plone.supermodel.directives import primary
from Products.CMFPlone.browser.search import quote_chars
from Products.CMFPlone.utils import safe_unicode
from Products.Five import BrowserView
from Products.ZCTextIndex.ParseTree import ParseError
from zope import schema
from zope.interface import Invalid

import re


MULTISPACE = u'\u3000'.encode('utf-8')
BAD_CHARS = ('?', '-', '+', '*', MULTISPACE)

checkEmail = re.compile(
    r'[a-zA-Z0-9._%-]+@([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,4}').match


def validateEmail(value):
    if not checkEmail(value):
        raise Invalid(_(safe_unicode('Invalid email address')))
    return True


class ITLCenter(model.Schema):
    """ A Templates Upload Center.
    """

    title = schema.TextLine(
        title=_(safe_unicode('Name of the Templates Center')),
    )

    description = schema.Text(
        title=_(safe_unicode('Description of the Templates Center')),
    )

    product_description = schema.Text(
        title=_(safe_unicode('Description of the features of templates')),
    )

    product_title = schema.TextLine(
        title=_(safe_unicode('Template Product Name')),
        description=_(safe_unicode(
            'Name of the Template product, e.g. only Templates')),
    )

    model.fieldset('categories_et_all',
                   label=_(safe_unicode('Categories et all')),
                   fields=['available_category', 'available_licenses',
                           'available_versions', 'available_platforms'])

    available_category = schema.List(title=_(safe_unicode('Available Categories')),
                                     default=['Business',
                                              ],
                                     value_type=schema.TextLine())

    available_licenses = schema.List(title=_(safe_unicode('Available Licenses')),
                                     default=[
                                         'GNU-GPL-v2 (GNU General Public'
                                         'License Version 2)',
                                         'GNU-GPL-v3+ (General Public License'
                                         'Version 3 and later)',
                                         'LGPL-v2.1 (GNU Lesser General'
                                         'Public License Version 2.1)',
                                         'LGPL-v3+ (GNU Lesser General Public'
                                         'License Version 3 and later)',
                                         'BSD (BSD License (revised))',
                                         'MPL-v1.1 (Mozilla Public License'
                                         'Version 1.1)',
                                         'MPL-v2.0+ (Mozilla Public License'
                                         'Version 2.0 or later)',
                                         'CC-by-sa-v3 (Creative Commons'
                                         'Attribution-ShareAlike 3.0)',
                                         'CC-BY-SA-v4 (Creative Commons'
                                         'Attribution-ShareAlike 4.0 '
                                         'International)',
                                         'AL-v2 (Apache License Version 2.0)'],
                                     value_type=schema.TextLine())

    available_versions = schema.List(title=_(safe_unicode('Available Versions')),
                                     default=['Product 1.0',
                                              ],
                                     value_type=schema.TextLine())

    available_platforms = schema.List(title=_(safe_unicode('Available Platforms')),
                                      default=['All platforms',
                                               'Linux',
                                               'Linux-x64',
                                               'Mac OS X',
                                               'Windows',
                                               'BSD',
                                               'UNIX (other)'],
                                      value_type=schema.TextLine())

    model.fieldset('allowedfileextensions',
                   label=_(safe_unicode('Allowed file extensions')),
                   fields=['allowed_fileextension',
                           'allowed_imageextension',
                           ],
                   )

    allowed_fileextension = schema.TextLine(
        title=_(safe_unicode('Allowed file extensions')),
        description=_(safe_unicode(
            'Fill in the allowed file extensions, seperated by '
            "a pipe '|'.")),
    )

    allowed_imageextension = schema.TextLine(
        title=_(safe_unicode('Allowed image file extension')),
        description=_(safe_unicode(
            'Fill in the allowed image file extensions, seperated '
            "by a pipe '|'.")),
    )

    model.fieldset('instructions',
                   label=_(safe_unicode('Instructions')),
                   fields=['install_instructions',
                           'reporting_bugs',
                           'information_oldversions',
                           ],
                   )

    primary('install_instructions')
    install_instructions = RichText(
        title=_(safe_unicode('Template installation instructions')),
        description=_(safe_unicode('Please fill in the install instructions')),
        required=False,
    )

    primary('reporting_bugs')
    reporting_bugs = RichText(
        title=_(safe_unicode('Instruction how to report Bugs')),
        required=False,
    )

    model.fieldset('disclaimer',
                   label=_(safe_unicode('Legal Disclaimer')),
                   fields=['title_legaldisclaimer', 'legal_disclaimer',
                           'title_legaldownloaddisclaimer',
                           'legal_downloaddisclaimer'])

    title_legaldisclaimer = schema.TextLine(
        title=_(safe_unicode('Title for Legal Disclaimer and Limitations')),
        default=_(safe_unicode('Legal Disclaimer and Limitations')),
        required=False,
    )

    legal_disclaimer = schema.Text(
        title=_(safe_unicode('Text of the Legal Disclaimer and Limitations')),
        description=_(safe_unicode(
            'Enter the text of the legal disclaimer and limitations that '
            'should be displayed to the project creator and should be '
            'accepted by the owner of the project.')),
        default=_(safe_unicode(
            'Fill in the legal disclaimer, that had to be accepted by the '
            'project owner')),
        required=False,
    )

    title_legaldownloaddisclaimer = schema.TextLine(
        title=_(safe_unicode(
            'Title of the Legal Disclaimer and Limitations for Downloads')),
        default=_(safe_unicode('Legal Disclaimer And Limitations For Downloads')),
        required=False,
    )

    primary('legal_downloaddisclaimer')
    legal_downloaddisclaimer = RichText(
        title=_(safe_unicode('Text of the Legal Disclaimer and Limitations for Downlaods')),
        description=_(safe_unicode(
            'Enter any legal disclaimer and limitations for downloads that '
            'should appear on each page for dowloadable files.')),
        default=_(safe_unicode('Fill in the text for the legal download disclaimer')),
        required=False,
    )

    primary('information_oldversions')
    information_oldversions = RichText(
        title=_(safe_unicode('Information about search for old product versions')),
        description=_(safe_unicode(
            'Enter an information about the search for older '
            'versions of the product, if they are not on the '
            'versions list (compatibility) anymore.')),
        required=False,
    )

    model.fieldset('contactadresses',
                   label=_(safe_unicode('Special email adresses')),
                   fields=['contactForCenter'])

    contactForCenter = schema.ASCIILine(
        title=_(safe_unicode(
            'EMail address for communication with the template center '
            'manager and reviewer')),
        description=_(
            u'Enter an email address for the communication with template '
            u'center manager and reviewer'),
        default='projects@foo.org',
        constraint=validateEmail,
    )


directives.languageindependent('available_category')
directives.languageindependent('available_licenses')
directives.languageindependent('available_versions')
directives.languageindependent('available_platforms')


class TLCenterView(BrowserView):

    def tlprojects(self):
        from collective.templates.tlproject import ITLProject
        context = aq_inner(self.context)
        catalog = api.portal.get_tool(name='portal_catalog')

        return catalog(object_provides=ITLProject.__identifier__,
                       path='/'.join(context.getPhysicalPath()),
                       sort_order='sortable_title')

    def get_latest_program_release(self):
        versions = list(self.context.available_versions)
        versions.sort(reverse=True)
        return versions[0]

    def category_name(self):
        category = list(self.context.available_category)
        return category

    def tlproject_count(self):
        """Return number of projects
        """
        catalog = api.portal.get_tool(name='portal_catalog')

        return len(catalog(portal_type='collective.templates.tlproject',
                           review_state='published'))

    def get_most_popular_products(self):
        catalog = api.portal.get_tool(name='portal_catalog')
        sort_on = 'positive_ratings'
        contentFilter = {
            'sort_on': sort_on,
            'sort_order': 'reverse',
            'review_state': 'published',
            'portal_type': 'collective.templates.tlproject'}
        return catalog(**contentFilter)

    def get_newest_products(self):
        sort_on = 'created'
        contentFilter = {
            'sort_on': sort_on,
            'sort_order': 'reverse',
            'review_state': 'published',
            'portal_type': 'collective.templates.tlproject',
        }

        results = api.content.find(**contentFilter)

        return results

    def get_products(self, category, version, sort_on, SearchableText=None):
        # sort_on = 'positive_ratings'
        if SearchableText:
            SearchableText = self.munge_search_term(SearchableText)
            contentFilter = {
                'sort_on': sort_on,
                'SearchableText': SearchableText,
                'sort_order': 'reverse',
                'portal_type': 'collective.templates.tlproject',
            }

        else:
            contentFilter = {
                'sort_on': sort_on,
                'sort_order': 'reverse',
                'portal_type': 'collective.templates.tlproject',
            }

        if version != 'any':
            contentFilter['getCompatibility'] = version

        if category:
            contentFilter['getCategories'] = category

        try:
            return api.content.find(**contentFilter)
        except ParseError:
            return []

    def munge_search_term(self, q):
        for char in BAD_CHARS:
            char = str(char)
            q = q.replace(char, ' ')
        r = q.split()
        r = ' AND '.join(r)
        r = quote_chars(r) + '*'
        return r

    def show_search_form(self):
        return 'getCategories' in self.request.environ['QUERY_STRING']


class TLCenterOwnProjectsViewlet(ViewletBase):

    def get_results(self):
        current_user = api.user.get_current()
        pc = api.portal.get_tool('portal_catalog')
        return pc.portal_catalog(
            portal_type='collective.templates.tlproject',
            sort_on='Date',
            sort_order='reverse',
            Creator=str(current_user))
