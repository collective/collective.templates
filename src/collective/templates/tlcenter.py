# -*- coding: utf-8 -*-
from collective.templates import _
from collective.templates.common import validateemail
from plone import api
from plone.app.layout.viewlets import ViewletBase
from plone.app.textfield import RichText
from plone.supermodel import model
from plone.supermodel.directives import primary
from Products.CMFPlone.browser.search import quote_chars
from Products.CMFPlone.utils import safe_unicode
from Products.Five import BrowserView
from Products.ZCTextIndex.ParseTree import ParseError
from zope import schema


MULTISPACE = u'\u3000'.encode('utf-8')
BAD_CHARS = ('?', '-', '+', '*', MULTISPACE)


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
        constraint=validateemail,
    )


class TLCenterView(BrowserView):

    def category_names(self):
        return list(api.portal.get_registry_record('collectivetemplates.available_category'))

    def version_names(self):
        return list(api.portal.get_registry_record('collectivetemplates.available_versions'))

    def get_latest_program_release(self):
        versions = list(api.portal.get_registry_record('collectivetemplates.available_versions'))
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
