# -*- coding: utf-8 -*-
from collective import dexteritytextindexer
from collective.templates import _
from collective.templates import quote_chars
from plone import api
from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.browser.view import DefaultView
from plone.namedfile.field import NamedBlobFile
from plone.namedfile.field import NamedBlobImage
from plone.supermodel import model
from plone.supermodel.directives import primary
from Products.validation import V_REQUIRED
from z3c.form import validator
from z3c.form.browser.checkbox import CheckBoxFieldWidget
from zope import schema
from zope.interface import directlyProvides
from zope.interface import Invalid
from zope.interface import invariant
from zope.interface import provider
from zope.schema.interfaces import IContextAwareDefaultFactory
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary

import re


checkemail = re.compile(
    r'[a-zA-Z0-9._%-]+@([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,4}').match


def validateemail(value):
    if not checkemail(value):
        raise Invalid(_(u'Invalid email address'))
    return True


def vocabavaillicenses(context):
    """ pick up licenses list from parent """
    from collective.templates.tlcenter import ITLCenter
    while context is not None and not ITLCenter.providedBy(context):
        # context = aq_parent(aq_inner(context))
        context = context.__parent__

    license_list = []
    if context is not None and context.available_licenses:
        license_list = context.available_licenses
    terms = []
    for value in license_list:
        terms.append(SimpleTerm(value, token=value.encode('unicode_escape'),
                                title=value))
    return SimpleVocabulary(terms)


directlyProvides(vocabavaillicenses, IContextSourceBinder)


def vocabcategories(context):
    # For add forms

    # For other forms edited or displayed
    from collective.templates.tlcenter import ITLCenter
    while context is not None and not ITLCenter.providedBy(context):
        # context = aq_parent(aq_inner(context))
        context = context.__parent__

    category_list = []
    if context is not None and context.available_category:
        category_list = context.available_category

    terms = []
    for value in category_list:
        terms.append(SimpleTerm(value, token=value.encode('unicode_escape'),
                                title=value))

    return SimpleVocabulary(terms)


directlyProvides(vocabcategories, IContextSourceBinder)


def vocabavailversions(context):
    """ pick up the program versions list from parent """
    from collective.templates.tlcenter import ITLCenter
    while context is not None and not ITLCenter.providedBy(context):
        # context = aq_parent(aq_inner(context))
        context = context.__parent__

    versions_list = []
    if context is not None and context.available_versions:
        versions_list = context.available_versions

    terms = []
    for value in versions_list:
        terms.append(SimpleTerm(value, token=value.encode('unicode_escape'),
                                title=value))
    return SimpleVocabulary(terms)


directlyProvides(vocabavailversions, IContextSourceBinder)


def vocabavailplatforms(context):
    """ pick up the list of platforms from parent """
    from collective.templates.tlcenter import ITLCenter
    while context is not None and not ITLCenter.providedBy(context):
        # context = aq_parent(aq_inner(context))
        context = context.__parent__

    platforms_list = []
    if context is not None and context.available_platforms:
        platforms_list = context.available_platforms
    terms = []
    for value in platforms_list:
        terms.append(SimpleTerm(value, token=value.encode('unicode_escape'),
                                title=value))
    return SimpleVocabulary(terms)


directlyProvides(vocabavailplatforms, IContextSourceBinder)


def isNotEmptyCategory(value):
    if not value:
        raise Invalid(u'You have to choose at least one category for your '
                      u'project.')
    return True


class AcceptLegalDeclaration(Invalid):
    __doc__ = _(u'It is necessary that you accept the Legal Declaration')


@provider(IContextAwareDefaultFactory)
def legal_declaration_title(context):
    return context.title_legaldisclaimer


@provider(IContextAwareDefaultFactory)
def legal_declaration_text(context):
    return context.legal_disclaimer


@provider(IContextAwareDefaultFactory)
def allowedtemplatefileextensions(context):
    return context.allowed_fileextension.replace("|", ", ")

@provider(IContextAwareDefaultFactory)
def allowedimagefileextensions(context):
    return context.allowed_imageextension.replace("|", ",")


def validatetemplatefileextension(value):
    catalog = api.portal.get_tool(name='portal_catalog')
    result=catalog.uniqueValuesFor('allowedfileextensions')
    pattern = r'^.*\.{0}'.format(result[0])
    matches = re.compile(pattern, re.IGNORECASE).match
    if not matches(value.filename):
        raise Invalid(
            u'You could only upload files with an allowed file extension. '
            u'Please try again to upload a file with the correct file'
            u'extension.')
    return True


def validateimagefileextension(value):
    catalog = api.portal.get_tool(name='portal_catalog')
    result=catalog.uniqueValuesFor('allowedimageextensions')
    pattern = r'^.*\.{0}'.format(result[0])
    matches = re.compile(pattern, re.IGNORECASE).match
    if not matches(value.filename):
        raise Invalid(
            u'You could only upload files with an allowed file extension. '
            u'Please try again to upload a file with the correct file'
            u'extension.')
    return True



class ITLProject(model.Schema):
    directives.mode(information='display')
    information = schema.Text(
        title=_(u'Information'),
        description=_(
            u'The Dialog to create a new project consists of different '
            u'register. Please go through this register and fill in the '
            u'appropriate data for your project or choose one of the '
            u'options that are provided. You could upload one or more files '
            u'to your project on the register \'File Upload\' and '
            u'\'Optional Further File Upload\'.'),
    )

    dexteritytextindexer.searchable('title')
    title = schema.TextLine(
        title=_(u'Title'),
        description=_(u'Project Title - minimum 5 and maximum 50 characters'),
        min_length=5,
        max_length=50,
    )

    dexteritytextindexer.searchable('description')
    description = schema.Text(
        title=_(u'Project Summary'),
    )

    dexteritytextindexer.searchable('details')
    primary('details')
    details = RichText(
        title=_(u'Full Project Description'),
        required=False,
    )

    directives.widget(licenses_choice=CheckBoxFieldWidget)
    licenses_choice = schema.List(
        title=_(u'License of the uploaded file'),
        description=_(
            u'Please mark one or more licenses under which you publish '
            u'your file(s).'),
        value_type=schema.Choice(source=vocabavaillicenses),
        required=True,
    )

    directives.mode(title_declaration_legal='display')
    title_declaration_legal = schema.TextLine(
        title=_(u''),
        required=False,
        defaultFactory=legal_declaration_title,
    )

    directives.mode(declaration_legal='display')
    declaration_legal = schema.Text(
        title=_(u''),
        required=False,
        defaultFactory=legal_declaration_text,
    )

    accept_legal_declaration = schema.Bool(
        title=_(u'Accept the above legal disclaimer'),
        description=_(
            u'Please declare that you accept the above legal disclaimer.'),
        required=True,
    )

    dexteritytextindexer.searchable('category_choice')
    directives.widget(category_choice=CheckBoxFieldWidget)
    category_choice = schema.List(
        title=_(u'Choose your categories'),
        description=_(
            u'Please select the appropriate categories (one or more) for '
            u'your project.'),
        value_type=schema.Choice(source=vocabcategories),
        constraint=isNotEmptyCategory,
        required=True,
    )

    contactAddress = schema.TextLine(
        title=_(u'Contact email-address'),
        description=_(u'Contact email-address for the project.'),
        constraint=validateemail,
    )


    directives.mode(timageextension='display')
    timageextension = schema.TextLine(
        title=_(u'The following file extensions are allowed for screenshot '
                u'files (upper case and lower case and mix of both):'),
        defaultFactory=allowedimagefileextensions,
    )

    screenshot = NamedBlobImage(
        title=_(u'Screenshot of the Tempate'),
        description=_(
            u'Add a screenshot by clicking the \'Browse\' button. You could '
            u'provide an image of the file format \'png\', \'gif\' or \'jpg\'.'),
        required=True,
        constraint=validateimagefileextension,
    )

    releasenumber = schema.TextLine(
        title=_(u'Versions Number'),
        description=_(
            u'Version Number of the Template File (up to twelf chars) '
            u'which you upload in this project.'),
        default=_(u'1.0'),
        max_length=12,
    )

    directives.widget(compatibility_choice=CheckBoxFieldWidget)
    compatibility_choice = schema.List(
        title=_(u'Compatible With Versions Of The Product'),
        description=_(
            u'Please mark one or more program versions with which this '
            u'uploaded file is compatible with.'),
        value_type=schema.Choice(source=vocabavailversions),
        required=True,
        default=[],
    )

    directives.mode(tfileextension='display')
    tfileextension = schema.TextLine(
        title=_(u'The following file extensions are allowed for template '
                u'files (upper case and lower case and mix of both):'),
        defaultFactory=allowedtemplatefileextensions,
    )

    file = NamedBlobFile(
        title=_(u'The first file you want to upload.'),
        description=_(u'Please upload your file.'),
        required=True,
        constraint=validatetemplatefileextension,
    )

    directives.widget(platform_choice=CheckBoxFieldWidget)
    platform_choice = schema.List\
        (
            title=_(u'First uploaded file is compatible with the Platform(s)'),
            description=_(
                u'Please mark one or more platforms with which the uploaded '
                u'file is compatible.'),
            value_type=schema.Choice(source=vocabavailplatforms),
            required=True,
        )

    directives.mode(filetitlefield='display')
    filetitlefield = schema.TextLine(
        title=_(u'The First File You Want To Upload'),
        description=_(
            u'You need only to upload one file to your project. There are '
            u'options for further two file uploads if you want to provide '
            u'files for different platforms.'),
    )

    model.fieldset('fileset2',
                   label=u'Optional Further File Upload',
                   fields=['filetitlefield1', 'platform_choice1',
                           'tfileextension1', 'file1',
                           'filetitlefield2', 'platform_choice2',
                           'tfileextension2', 'file2'],
                   )

    directives.mode(filetitlefield1='display')
    filetitlefield1 = schema.TextLine(
        title=_(u'The second file you want to upload.'),
        description=_(
            u'Here you could add an optional second file to your project, if '
            u'the files support different platforms.'),
    )

    directives.widget(platform_choice1=CheckBoxFieldWidget)
    platform_choice1 = schema.List(
        title=_(u'Second uploaded file is compatible with the Platform(s)'),
        description=_(
            u'Please mark one or more platforms with which the uploaded file '
            u'is compatible.'),
        value_type=schema.Choice(source=vocabavailplatforms),
        required=False,
    )


    directives.mode(tfileextension1='display')
    tfileextension1 = schema.TextLine(
        title=_(u'The following file extensions are allowed for template '
                u'files (upper case and lower case and mix of both):'),
        defaultFactory=allowedtemplatefileextensions,
    )

    file1 = NamedBlobFile(
        title=_(u'The second file you want to upload (this is optional)'),
        description=_(u'Please upload your file.'),
        required=False,
        constraint=validatetemplatefileextension,
    )

    directives.mode(filetitlefield2='display')
    filetitlefield2 = schema.TextLine(
        title=_(u'The third file you want to upload'),
        description=_(
            u'Here you could add an optional third file to your project, if '
            u'the files support different platforms.'),
    )

    directives.widget(platform_choice2=CheckBoxFieldWidget)
    platform_choice2 = schema.List(
        title=_(u'Third uploaded file is compatible with the Platform(s))'),
        description=_(
            u'Please mark one or more platforms with which the uploaded file '
            u'is compatible.'),
        value_type=schema.Choice(source=vocabavailplatforms),
        required=False,
    )


    directives.mode(tfileextension2='display')
    tfileextension2 = schema.TextLine(
        title=_(u'The following file extensions are allowed for template '
                u'files (upper case and lower case and mix of both):'),
        defaultFactory=allowedtemplatefileextensions,
    )

    file2 = NamedBlobFile(
        title=_(u'The third file you want to upload (this is optional)'),
        description=_(u'Please upload your file.'),
        required=False,
        constraint=validatetemplatefileextension,
    )


@invariant
def licensenotchoosen(value):
    if not value.licenses_choice:
        raise Invalid(_(u'Please choose a license for the file(s) you want to'
                        u'upload.'))


@invariant
def compatibilitynotchoosen(data):
    if not data.compatibility_choice:
        raise Invalid(_(
            u'Please choose one or more compatible product versions for '
            u'the file(s) you want to upload.'))


@invariant
def legaldeclarationaccepted(data):
    if data.accept_legal_declaration is not True:
        raise AcceptLegalDeclaration(
            _(
                u'Please accept the Legal Declaration about your file(s) '
                u'and your Uploaded File'))


@invariant
def noOSChosen(data):
    if data.file is not None and data.platform_choice == []:
        raise Invalid(_(
            u'Please choose a compatible platform for the uploaded file.'))


def notifyAboutNewProject(self, event):
    if self.__parent__.contactForCenter is not None:
        mailrecipient = str(self.__parent__.contactForCenter)
    else:
        mailrecipient = api.portal.get_registry_record('plone.email_from_address')
    api.portal.send_email(
        recipient=mailrecipient,
        subject=(u'A Project with the title {0} was added').format(self.title),
        body='A member added a new project',
    )


def notifyProjectManager(self, event):
    state = api.content.get_state(self)
    if self.__parent__.contactForCenter is not None:
        mailsender = str(self.__parent__.contactForCenter)
    else:
        mailsender = api.portal.get_registry_record('plone.email_from_address')
    api.portal.send_email(
        recipient=('{0}').format(self.contactAddress),
        sender=(u'{0} <{1}>').format('Admin of the Website', mailsender),
        subject=(u'Your Project {0}').format(self.title),
        body=(
            u'The status of your templates project changed. '
            u'The new status is {0}').format(state),
    )


def notifyAboutNewReviewlistentry(self, event):
    state = api.content.get_state(self)
    if self.__parent__.contactForCenter is not None:
        mailrecipient = str(self.__parent__.contactForCenter)
    else:
        mailrecipient = api.portal.get_registry_record('plone.email_from_address')
    if state == 'pending':
        api.portal.send_email(
            recipient=mailrecipient,
            subject=(
                u'A Project with the title {0} was added to the review '
                u'list').format(self.title),
            body='Please have a look at the review list and check if the '
                 'project is ready for publication. \n'
                 '\n'
                 'Kind regards,\n'
                 'The Admin of the Website',
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
                    raise Invalid(_(u'The project title is already in use.'))


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
