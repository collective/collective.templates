# -*- coding: utf-8 -*-
from collective.templates import _
from plone.app.multilingual.dx import directives
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.base.utils import safe_text
from plone.supermodel import model
from plone.z3cform import layout
from zope import schema
from zope.interface import Interface


class ICollectivetemplatesControlPanel(Interface):
    available_category = schema.Tuple(title=_(
        safe_text('Available Categories')),
            default=('Business',),
            value_type=schema.TextLine())

    available_licenses = schema.Tuple(title=_(
        safe_text('Available Licenses')),
            default=(
                'GNU-GPL-v2 (GNU General Public License Version 2)',
                'GNU-GPL-v3+ (General Public License Version 3 and later)',
                'LGPL-v2.1 (GNU Lesser General Public License Version 2.1)',
                'LGPL-v3+ (GNU Lesser General Public License Version 3 '
                'and later)',
                'BSD (BSD License (revised))',
                'MPL-v1.1 (Mozilla Public License'
                'Version 1.1)',
                'MPL-v2.0+ (Mozilla Public License Version 2.0 or later)',
                'CC-by-sa-v3 (Creative Commons Attribution-ShareAlike 3.0)',
                'CC-BY-SA-v4 (Creative Commons Attribution-ShareAlike 4.0 '
                'International)',
                'AL-v2 (Apache License Version 2.0)'),
            value_type=schema.TextLine())

    available_versions = schema.Tuple(title=_(
        safe_text('Available Versions')),
            default=('Product 1.0',),
            value_type=schema.TextLine())

    available_platforms = schema.Tuple(title=_(
        safe_text('Available Platforms')),
            default=(
                'All platforms',
                'Linux',
                'Linux-x64',
                'Mac OS X',
                'Windows',
                'BSD',
                'UNIX (other)'),
            value_type=schema.TextLine())

    model.fieldset('allowedfileextensions',
                   label=_(safe_text('Allowed file extensions')),
                   fields=['allowed_templatefileextension',
                           'allowed_tempimageextension',
                           ],
                   )

    allowed_templatefileextension = schema.TextLine(
        title=_(safe_text('Allowed template file extensions')),
        description=_(safe_text(
            'Fill in the allowed file extensions, seperated by '
            "a pipe '|'.")),
        default=safe_text('ott|ots|otp|otg'),
    )

    allowed_tempimageextension = schema.TextLine(
        title=_(safe_text('Allowed image file extension')),
        description=_(safe_text(
            'Fill in the allowed image file extensions, seperated '
            "by a pipe '|'.")),
        default=safe_text('jpg|jpeg|png|gif'),
    )

    model.fieldset('disclaimer',
                   label=u'Legal Disclaimer',
                   fields=['title_legaldisclaimer', 'legal_disclaimer',
                           'title_legaldownloaddisclaimer',
                           'legal_downloaddisclaimer'])

    title_legaldisclaimer = schema.TextLine(
        title=_(safe_text('Title for Legal Disclaimer and Limitations')),
        default=_(safe_text('Legal Disclaimer and Limitations')),
        required=False,
    )

    legal_disclaimer = schema.Text(
        title=_(safe_text('Text of the Legal Disclaimer and Limitations')),
        description=_(safe_text(
            'Enter the text of the legal disclaimer and limitations that '
            'should be displayed to the project creator and should be '
            'accepted by the owner of the project.')),
        default=_(safe_text(
            'Fill in the legal disclaimer, that had to be accepted by the '
            'project owner')),
        required=False,
    )

    title_legaldownloaddisclaimer = schema.TextLine(
        title=_(safe_text(
            'Title of the Legal Disclaimer and Limitations for Downloads')),
        default=_(safe_text(
            'Legal Disclaimer And Limitations For Downloads')),
        required=False,
    )

    legal_downloaddisclaimer = schema.Text(
        title=_(safe_text(
            'Text of the Legal Disclaimer and Limitations for Downlaods')),
        description=_(safe_text(
            'Enter any legal disclaimer and limitations for downloads that '
            'should appear on each page for dowloadable files.')),
        default=_(safe_text(
            'Fill in the text for the legal download disclaimer')),
        required=False,
    )


directives.languageindependent('available_category')
directives.languageindependent('available_licenses')
directives.languageindependent('available_versions')
directives.languageindependent('available_platforms')


class CollectivetemplatesControlPanelForm(RegistryEditForm):
    schema = ICollectivetemplatesControlPanel
    schema_prefix = 'collectivetemplates'
    label = u'Collective Templates Settings'


CollectivetemplatesControlPanelView = layout.wrap_form(
    CollectivetemplatesControlPanelForm, ControlPanelFormWrapper)
