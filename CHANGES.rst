Changelog
=========


3.2 (2021-12-25)
----------------

- This release applied the changes, which where made with
  release 2.6 to 2.8 upon release 2.5, to the release
  line 3.x. The changes of release 3.2 were the same as
  listed for the releases 2.6, 2.7 and 2.8 in total
  (see for details the entries for this releases
  below) [Andreas Mantke]


2.8 (2021-12-25)
----------------

- Use mode instead of direction down for image rendering
  on project view because of a Deprecation warning [Andreas Mantke]
- Add restapi endpoints for portal_catalog search for
  categories, release compatibility, licenses, email address
  and name public [Andreas Mantke]
- Update localization files [Andreas Mantke]


2.7 (2021-12-16)
----------------

- Fix renaming issues especially in functions in the modules
  mailtoauthor and mailtoprojectowner as well as the
  tlcenter view [Andreas Mantke]
- Update localization files [Andreas Mantke]


2.6 (2021-12-15)
----------------

- Use Github actions and add a workflow script for building
  and testing [Andreas Mantke]
- Improve naming of the test-plone cfg-files [Andreas Mantke]
- Use the schema field Email instead of a TextLine field
  with an own constraint script [Andreas Mantke]
- Rename the content types for template center and
  template project for compatibility with the new Plone 6
  frontend Volto [Andreas Mantke]
- Rework of the views to work with the new naming of the
  custom content types [Andresa Mantke]
- Update localization files [Andreas Mantke]


3.1 (2021-09-23)
----------------

- This release applied the changes, which where made with
  release 2.5 upon release 2.4 to the release line 3.x. The
  changes of release 3.1 were the same as listed for release
  2.5 (see below) [Andreas Mantke]


2.5 (2021-09-23)
----------------

- Use Products.PrintingMailHost 1.1.6 for compatibility with
  Python 3.9 [Andreas Mantke]
- Add Python 3.8 and 3.9 to the classifiers [Andreas Mantke]
- Remove not used function tlprojects from the view of the
  tlcenter [Andreas Mantke]
- Update localization files [Andreas Mantke]
- Fix validation functions in the common module [Andreas Mantke]


3.0 (2021-07-31)
----------------

- Change the main release number to 3.x because this version
  breakes compatibility due to move to honeypot instead of
  captcha technology to protect mail forms. [Andreas Mantke]
- Update README with information about honeypot technology
  [Andreas Mantke]
- Add contactauthor and contactprojectowner module with
  honeypot technology to protect against robots, add
  collective.honeypot to the requirements. [Andreas Mantke]
- Add configuration for collective.honeypot to the
  buildout script. [Andreas Mantke]
- Remove mailtoauthor and mailtoprojectowner modules with
  hcaptcha technology and plone.formwidget.hcaptcha from
  the requirements. [Andreas Mantke]


2.4 (2021-07-31)
----------------

- Fix of the get_latest_program_release function
  and remove not any more used import. [Andreas Mantke]
- Update localization files [Andreas Mantke]


2.3 (2021-07-27)
----------------

- Add PloneHotfix to the buildout [Andreas Mantke]
- Migrate mail forms from plone.formwidget.recaptcha to
  plone.formwidget.hcaptcha and revome the recaptcha
  Plone add-on from the buildout [Andreas Mantke]
- Add PrintingMailHost to the buildout [Andreas Mantke]


2.2 (2020-11-13)
----------------

- Add listing of the number of projects per category to the sidebar of the
  templatecenters view template [Andreas Mantke]
- Update localization files [Andreas Mantke]


2.1 (2020-09-27)
----------------

- Reordering view templates and move them to one new folder [Andreas Mantke]
- Update localization files [Andreas Mantke]


2.0 (2020-07-29)
----------------

- Add a controlpanel and move configuration entries from the templatecenter
  module to this panel, create new vocabulary and functions from this
  entries in the configuration registry instead of entries in the portal_catalog,
  register vocabularies as named utilities in the configure.zcml file, use the
  new functions (inside the common module) for the project creation / edit
  form and their views as well as for the search feature of the template
  center module. [Andreas Mantke]
- Update localization files and German localization [Andreas Mantke]
- Adapt the user documentation to the new functions and structure of the
  add-on and create documentation in html and pdf file format [Andreas Mantke]
- Use safe_unicode for unicode strings, make more labels translatable [Andreas Mantke]
- Update README.rst [Andreas Mantke]


1.2.1 (2020-05-07)
------------------

- Fix strings in tlproject module [Andreas Mantke]
- Change tests about publication of project owner
  name and contact e-mail in the tlproject view template
  to more secure and explicit expression [Andreas Mantke]
- Update localization files and German localization of
  new strings [Andreas Mantke]


1.2 (2020-05-03)
----------------

- Add information about getting in contact with project owners/main
  contacts to the documentation and update the user documentation in
  html and pdf file format [Andreas Mantke]
- Add fields to choose if the e-mail address and / or the name of the
  project owner should be displayed on the project page and index the
  selection in the portal_catalog. Create a catalog query to get the
  appropriate value from the catalog and use it to manage the display
  of the data on the project website. [Andreas Mantke]
- Update localization files and localization into German [Andreas Mantke]


1.1 (2020-03-25)
----------------

- Add information about buildout entries and update documentation
  in HTML and PDF file format. [Andreas Mantke]
- Add versions to test_plone52.cfg [Andreas Mantke]
- Add a messaging to the admin or a special address for the
  edits of published project to prevent from misuse [Andreas Mantke]
- Improve the mail to template author form and add a new module for a
  contact with the project owner, add a link to the mail forms from
  template project respective the template center view. [Andreas Mantke]
- Update localization files [Andreas Mantke]


1.0 (2019-11-30)
----------------

- Complete user documentation [Andreas Mantke]
- Flake8 fixes [Andreas Mantke]
- Add a custom.css for creating documentation in HTML file
  format [Andresa Mantke]
- Update Manifest.in [Andreas Mantke]
- Update localization files [Andreas Mantke]


1.0b0 (2019-09-10)
------------------

- Made additions to travis.yml to get the robot test running
  successfully [Andreas Mantke]
- Update the Readme and add more features of the add-on [Andreas Mantke]


1.0a8 (2019-09-01)
------------------

- Activate include dependencies in configure.zcml [Andreas Mantke]
- Remove Travis test for Plone 4.3 [Andreas Mantke]
- Send notifications about a new product version only to the
  project email address instead of all users of the site [Andreas Mantke]


1.0a7 (2019-08-30)
------------------

- Fix the content type in the search for own projects in the
  own projects viewlet [Andreas Mantke]
- Improve the message to the sender of a author contact
  form [Andreas Mantke]
- Update localization files [Andreas Mantke]


1.0a6 (2019-08-26)
------------------

- Improve the edit view of the tlcenter and the tlproject
  with further register and reordered fields. [Andreas Mantke]
- Update localization files [Andreas Mantke]


1.0a5 (2019-08-25)
------------------

- Pep8 and other code fixes [Andreas Mantke]
- Change the sender of the messages to the portal email
  address [Andreas Mantke]
- Use api.content.find instead of api.portal.get_tool for
  portal_catalog searches [Andreas Mantke]
- Update localization files [Andreas Mantke]


1.0a4 (2019-08-16)
------------------

- Fix rendering for DefaultView of projects [Andreas Mantke]
- Fix regular expressions for validation of file extensions [Andreas Mantke]
- Update localization template and localization files and add
  translation into German for further strings [Andreas Mantke]


1.0a3 (2019-08-11)
------------------

- Change the tag for rendering a RichText field in the template
  view page template [Andreas Mantke]
- Use safe_unicode util for strings in the mailtoauthor
  form [Andreas Mantke]


1.0a2 (2019-07-29)
------------------

- Improve Manifest.in [Andreas Mantke]
- Remove replaced functions from the tlproject module [Andreas Mantke]
- Remove default values for allowed file extensions [Andreas Mantke]
- Use only the first value of the catalog search result tuple
  for the pattern of the regular expression [Andreas Mantke]
- Update localization template file and localization
  files [Andreas Mantke]


1.0a1 (2019-07-09)
------------------

- Initial release.
  [andreasma]
