# -*- coding: utf-8 -*-
from collective import dexteritytextindexer
from collective.templates import _
from collective.templates import quote_chars
from collective.templates.common import allowedtempimageextensions
from collective.templates.common import allowedtemplatefileextensions
from collective.templates.common import legaldeclarationtext
from collective.templates.common import legaldeclarationtitle
from collective.templates.common import validateimagefileextension
from collective.templates.common import validatetemplatefileextension
from collective.templates.common import yesnochoice
from plone import api
from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.browser.view import DefaultView
from plone.namedfile.field import NamedBlobFile
from plone.namedfile.field import NamedBlobImage
from plone.schema.email import Email
from plone.supermodel import model
from plone.supermodel.directives import primary
from Products.CMFPlone.utils import safe_unicode
from Products.validation import V_REQUIRED  # noqa
from z3c.form import validator
from z3c.form.browser.checkbox import CheckBoxFieldWidget
from zope import schema
from zope.interface import Invalid
from zope.interface import invariant


def isNotEmptyCategory(value):
    if not value:
        raise Invalid(u'You have to choose at least one category for your '
                      u'project.')
    return True


class AcceptLegalDeclaration(Invalid):
    __doc__ = _(u'It is necessary that you accept the Legal Declaration')


class ITLProject(model.Schema):
    directives.mode(information='display')
    information = schema.Text(
        title=_(safe_unicode('Information')),
        description=(safe_unicode(
            'The Dialog to create a new project consists of different '
            'register. Please go through this register and fill in the '
            'appropriate data for your project or choose one of the '
            'options that are provided. You could upload one or more files '
            "to your project on the register 'File Upload' and "
            "'Optional Further File Upload'.")),
    )

    dexteritytextindexer.searchable('title')
    title = schema.TextLine(
        title=_(safe_unicode('Title')),
        description=_(safe_unicode('Project Title - minimum 5 and maximum 50 characters')),
        min_length=5,
        max_length=50,
    )

    dexteritytextindexer.searchable('description')
    description = schema.Text(
        title=_(safe_unicode('Project Summary')),
    )

    dexteritytextindexer.searchable('details')
    primary('details')
    details = RichText(
        title=_(safe_unicode('Full project description')),
        required=False,
    )

    model.fieldset('legal',
                   label=_(safe_unicode('Legal')),
                   fields=['licenses_choice',
                           'title_declaration_legal',
                           'declaration_legal',
                           'accept_legal_declaration',
                           ],
                   )

    directives.widget(licenses_choice=CheckBoxFieldWidget)
    licenses_choice = schema.List(
        title=_(safe_unicode('License of the uploaded file')),
        description=_(safe_unicode(
            'Please mark one or more licenses under which you publish '
            'your file(s).')),
        value_type=schema.Choice(source='Templatelicenses'),
        required=True,
    )

    directives.mode(title_declaration_legal='display')
    title_declaration_legal = schema.TextLine(
        title=_(safe_unicode('')),
        required=False,
        defaultFactory=legaldeclarationtitle,
    )

    directives.mode(declaration_legal='display')
    declaration_legal = schema.Text(
        title=_(safe_unicode('')),
        required=False,
        defaultFactory=legaldeclarationtext,
    )

    accept_legal_declaration = schema.Bool(
        title=_(safe_unicode('Accept the above legal disclaimer')),
        description=_(safe_unicode(
            'Please declare that you accept the above legal disclaimer.')),
        required=True,
    )

    model.fieldset('category',
                   label=_(safe_unicode('Category / Categories')),
                   fields=['category_choice'],
                   )

    dexteritytextindexer.searchable('category_choice')
    directives.widget(category_choice=CheckBoxFieldWidget)
    category_choice = schema.List(
        title=_(safe_unicode('Choose your categories')),
        description=_(safe_unicode(
            'Please select the appropriate categories (one or more) for '
            'your project.')),
        value_type=schema.Choice(source='Templatecategories'),
        constraint=isNotEmptyCategory,
        required=True,
    )

    templatecontactAddress = Email(
        title=_(safe_unicode('Contact email-address')),
        description=_(safe_unicode('Contact email-address for the project.')),
    )

    make_template_contact_address_public = schema.Choice(
        title=_(safe_unicode('Email Public?')),
        description=_(safe_unicode(
            'Please decide if your email address '
            'should be displayed on the project website.')),
        vocabulary=yesnochoice,
        required=True,
    )

    display_user_name = schema.Choice(
        title=_(safe_unicode('Project Author Public?')),
        description=_(safe_unicode(
            'Please decide if your name '
            'should be displayed on the project website.')),
        vocabulary=yesnochoice,
        required=True,
    )

    model.fieldset('screenshot',
                   label=_(safe_unicode('Screenshot')),
                   fields=['timageextension',
                           'screenshot',
                           ],
                   )

    directives.mode(timageextension='display')
    timageextension = schema.TextLine(
        title=_(safe_unicode(
            'The following file extensions are allowed for screenshot '
            'files (upper case and lower case and mix of both):')),
        defaultFactory=allowedtempimageextensions,
    )

    screenshot = NamedBlobImage(
        title=_(safe_unicode('Sreenshot of the Template')),
        description=_(safe_unicode(
            "Add a screenshot by clicking the 'Browse' button. You could "
            "provide an image of the file format 'png', 'gif' or "
            "'jpg'.")),
        required=True,
        constraint=validateimagefileextension,
    )

    releasenumber = schema.TextLine(
        title=_(safe_unicode('Versions Number')),
        description=_(safe_unicode(
            'Version Number of the Template File (up to twelf chars) '
            'which you upload in this project.')),
        default=_(safe_unicode('1.0')),
        max_length=12,
    )

    model.fieldset('compatibilty',
                   label=_(safe_unicode('Compatibility')),
                   fields=['compatibility_choice',
                           ],
                   )

    directives.widget(compatibility_choice=CheckBoxFieldWidget)
    compatibility_choice = schema.List(
        title=_(safe_unicode('Comatible with versions of the product')),
        description=_(safe_unicode(
            'Please mark one or more program versions with which this '
            'uploaded file is compatible with.')),
        value_type=schema.Choice(source='Templateversions'),
        required=True,
        default=[],
    )

    model.fieldset('fileset1',
                   label=_(safe_unicode('File Upload')),
                   fields=['filetitlefield',
                           'tfileextension',
                           'file',
                           'platform_choice',
                           ],
                   )

    directives.mode(filetitlefield='display')
    filetitlefield = schema.TextLine(
        title=_(safe_unicode('The first file you want to upload')),
        description=_(safe_unicode(
            'You need only to upload one file to your project. There are '
            'options for further two file uploads if you want to provide '
            'files for different platforms.')),
        required=False,
    )

    directives.mode(tfileextension='display')
    tfileextension = schema.TextLine(
        title=_(safe_unicode(
            'The following file extensions are allowed for template '
            'files (upper case and lower case and mix of both):')),
        defaultFactory=allowedtemplatefileextensions,
    )

    file = NamedBlobFile(
        title=_(safe_unicode('The first file you want to upload.')),
        description=_(safe_unicode('Please upload your file.')),
        required=True,
        constraint=validatetemplatefileextension,
    )

    directives.widget(platform_choice=CheckBoxFieldWidget)
    platform_choice = schema.List(
        title=_(safe_unicode('First uploaded file is compatible with the Platform(s)')),
        description=_(safe_unicode(
            'Please mark one or more platforms with which the uploaded '
            'file is compatible.')),
        value_type=schema.Choice(source='Templateplatforms'),
        required=True,
    )

    model.fieldset('fileset2',
                   label=_(safe_unicode('Optional Further File Upload')),
                   fields=['filetitlefield1', 'platform_choice1',
                           'tfileextension1', 'file1',
                           'filetitlefield2', 'platform_choice2',
                           'tfileextension2', 'file2'],
                   )

    directives.mode(filetitlefield1='display')
    filetitlefield1 = schema.TextLine(
        title=_(safe_unicode('The second file you want to upload.')),
        description=_(safe_unicode(
            'Here you could add an optional second file to your project, if '
            'the files support different platforms.')),
    )

    directives.widget(platform_choice1=CheckBoxFieldWidget)
    platform_choice1 = schema.List(
        title=_(safe_unicode('Second uploaded file is compatible with the Platform(s)')),
        description=_(safe_unicode(
            'Please mark one or more platforms with which the uploaded file '
            'is compatible.')),
        value_type=schema.Choice(source='Templateplatforms'),
        required=False,
    )

    directives.mode(tfileextension1='display')
    tfileextension1 = schema.TextLine(
        title=_(safe_unicode(
            'The following file extensions are allowed for template '
            'files (upper case and lower case and mix of both):')),
        defaultFactory=allowedtemplatefileextensions,
    )

    file1 = NamedBlobFile(
        title=_(safe_unicode('The second file you want to upload (this is optional)')),
        description=_(safe_unicode('Please upload your file.')),
        required=False,
        constraint=validatetemplatefileextension,
    )

    directives.mode(filetitlefield2='display')
    filetitlefield2 = schema.TextLine(
        title=_(safe_unicode('The third file you want to upload')),
        description=_(safe_unicode(
            'Here you could add an optional third file to your project, if '
            'the files support different platforms.')),
    )

    directives.widget(platform_choice2=CheckBoxFieldWidget)
    platform_choice2 = schema.List(
        title=_(safe_unicode('Third uploaded file is compatible with the Platform(s))')),
        description=_(safe_unicode(
            'Please mark one or more platforms with which the uploaded file '
            'is compatible.')),
        value_type=schema.Choice(source='Templateplatforms'),
        required=False,
    )

    directives.mode(tfileextension2='display')
    tfileextension2 = schema.TextLine(
        title=_(safe_unicode(
            'The following file extensions are allowed for template '
            'files (upper case and lower case and mix of both):')),
        defaultFactory=allowedtemplatefileextensions,
    )

    file2 = NamedBlobFile(
        title=_(safe_unicode('The third file you want to upload (this is optional)')),
        description=_(safe_unicode('Please upload your file.')),
        required=False,
        constraint=validatetemplatefileextension,
    )


@invariant
def licensenotchoosen(value):
    if not value.licenses_choice:
        raise Invalid(_(safe_unicode(
            'Please choose a license for the file(s) you want to'
            'upload.')))


@invariant
def compatibilitynotchoosen(data):
    if not data.compatibility_choice:
        raise Invalid(_(safe_unicode(
            'Please choose one or more compatible product versions for '
            'the file(s) you want to upload.')))


@invariant
def legaldeclarationaccepted(data):
    if data.accept_legal_declaration is not True:
        raise AcceptLegalDeclaration(
            _(safe_unicode(
                'Please accept the Legal Declaration about your file(s) '
                'and your Uploaded File')))


@invariant
def noOSChosen(data):
    if data.file is not None and data.platform_choice == []:
        raise Invalid(_(safe_unicode(
            'Please choose a compatible platform for the uploaded file.')))


def notifyAboutNewProject(self, event):
    if self.__parent__.contactForCenter is not None:
        mailrecipient = str(self.__parent__.contactForCenter)
    else:
        mailrecipient = api.portal.get_registry_record(
            'plone.email_from_address')
    api.portal.send_email(
        recipient=mailrecipient,
        subject=(safe_unicode('A Project with the title {0} was added')).format(self.title),
        body='A member added a new project',
    )


def notifyProjectManager(self, event):
    state = api.content.get_state(self)
    if self.__parent__.contactForCenter is not None:
        mailsender = str(self.__parent__.contactForCenter)
    else:
        mailsender = api.portal.get_registry_record('plone.email_from_address')
    api.portal.send_email(
        recipient=('{0}').format(self.templatecontactAddress),
        sender=(safe_unicode('{0} <{1}>')).format('Admin of the Website', mailsender),
        subject=(safe_unicode('Your Project {0}')).format(self.title),
        body=(safe_unicode(
            'The status of your templates project changed. '
            'The new status is {0}')).format(state),
    )


def notifyAboutNewReviewlistentry(self, event):
    state = api.content.get_state(self)
    if self.__parent__.contactForCenter is not None:
        mailrecipient = str(self.__parent__.contactForCenter)
    else:
        mailrecipient = api.portal.get_registry_record(
            'plone.email_from_address')
    if state == 'pending':
        api.portal.send_email(
            recipient=mailrecipient,
            subject=(safe_unicode(
                'A Project with the title {0} was added to the review '
                'list')).format(self.title),
            body='Please have a look at the review list and check if the '
                 'project is ready for publication. \n'
                 '\n'
                 'Kind regards,\n'
                 'The Admin of the Website',
        )


def textmodified_project(self, event):
    state = api.content.get_state(self)
    if (self.__parent__.contactForCenter) is not None:
        mailrecipient = str(self.__parent__.contactForCenter)
    else:
        mailrecipient = api.portal.get_registry_record(
            'plone.email_from_address')
    if state == 'published':
        if self.details is not None:
            detailed_description = self.details.output
        else:
            detailed_description = None

        api.portal.send_email(
            recipient=mailrecipient,
            sender=(u'{0} <{1}>').format(
                'Admin of the Website', mailrecipient),
            subject=(safe_unicode('The content of the project {0} has '
                                  'changed')).format(self.title),
            body=(safe_unicode('The content of the project {0} has changed. Here you get '
                               'the text of the description field of the '
                               "project: \n'{1}\n\nand this is the text of the "
                               "details field:\n{2}'")).format(self.title,
                                                               self.description,
                                                               detailed_description),
        )


class ValidateTLProjectUniqueness(validator.SimpleFieldValidator):
    # Validate site-wide uniqueness of project titles.

    def validate(self, value):
        # Perform the standard validation first

        super(ValidateTLProjectUniqueness, self).validate(value)
        if value is not None:
            catalog = api.portal.get_tool(name='portal_catalog')
            results = catalog({'Title': quote_chars(value),
                               'object_provides':
                                   ITLProject.__identifier__})
            contextUUID = api.content.get_uuid(self.context)
            for result in results:
                if result.UID != contextUUID:
                    raise Invalid(_(safe_unicode('The project title is already in use.')))


validator.WidgetValidatorDiscriminators(
    ValidateTLProjectUniqueness,
    field=ITLProject['title'],
)


class TLProjectView(DefaultView):
    def canPublishContent(self):
        return api.user.has_permission('cmf.ModifyPortalContent', self.context)

    def releaseLicense(self):
        catalog = api.portal.get_tool(name='portal_catalog')
        path = '/'.join(self.context.getPhysicalPath())
        idx_data = catalog.getIndexDataForUID(path)
        licenses = idx_data.get('releaseLicense')
        return (r for r in licenses)

    def projectCategory(self):
        catalog = api.portal.get_tool(name='portal_catalog')
        path = '/'.join(self.context.getPhysicalPath())
        idx_data = catalog.getIndexDataForUID(path)
        category = idx_data.get('getCategories')
        return (r for r in category)

    def releaseCompatibility(self):
        catalog = api.portal.get_tool(name='portal_catalog')
        path = '/'.join(self.context.getPhysicalPath())
        idx_data = catalog.getIndexDataForUID(path)
        compatibility = idx_data.get('getCompatibility')
        return (r for r in compatibility)

    def email_public(self):
        catalog = api.portal.get_tool(name='portal_catalog')
        path = '/'.join(self.context.getPhysicalPath())
        idx_data = catalog.getIndexDataForUID(path)
        public_email = idx_data.get('publicemail')
        return (public_email)

    def name_public(self):
        catalog = api.portal.get_tool(name='portal_catalog')
        path = '/'.join(self.context.getPhysicalPath())
        idx_data = catalog.getIndexDataForUID(path)
        public_name = idx_data.get('publicname')
        return (public_name)

    def title_download_disclaimer(self):
        return api.portal.get_registry_record('collectivetemplates.title_legaldownloaddisclaimer')

    def text_download_disclaimer(self):
        return api.portal.get_registry_record('collectivetemplates.legal_downloaddisclaimer')
