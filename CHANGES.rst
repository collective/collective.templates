Changelog
=========


1.0a9 (unreleased)
------------------

- Nothing changed yet.



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
