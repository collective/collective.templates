.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

====================
collective.templates
====================

Collective.templates adds a folder to Plone where users could upload document templates
and set categories e.g. compatibility, license. It's also possible to rate the templates
and give feedback to the template authors.

Features
--------

- A template center with listing and display of template projects respectively to their rating,
  a search form and a listing of the latest projects.
- Template projects with the abbility to upload template files and replace them with newer ones.
  The project page contains fields for product versions, categories, licenses and plattforms.
- The user could send a message to the author of a template via a mail. The mail form uses a
  recaptcha widget. The contact data of the author of the template will not be made public.
- The file extensions of the uploaded templates will be checked. It is possible to set the
  allowed file extensions distinct for the specific use case of the template center. They
  could be dynamically changed at any time.


Examples
--------

This add-on can be seen in action at the following sites:
-


Documentation
-------------

Full documentation for end users can be found in the "docs" folder, and is also available online at


Translations
------------

This product has been translated into

-


Installation
------------

Install collective.templates by adding it to your buildout::

    [buildout]

    ...

    eggs =
        collective.templates


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/collective/collective.templates/issues
- Source Code: https://github.com/collective/collective.templates
- Documentation: https://docs.plone.org/foo/bar


Support
-------

If you are having issues, please let us know.
We have a mailing list located at:


License
-------

The project is licensed under the GPLv2.
