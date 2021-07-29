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

- The add-on has a cofiguration settings entry in the site administration yet. It's form
  contains fields to set a choice of categories, platforms, licenses and versions of the
  product (for which the templates are used). There are also fields to set the allowed file
  extensions of the template files, the image files (e.g. screenshots, logos) and the
  documentation.
- A template center with listing and display of template projects respectively to their rating,
  a search form and a listing of the latest projects.
- The template center edit form contains fields to set the title of the center and the name of
  the templates and add a description of the center.
- Template projects with the abbility to upload template files and replace them with newer ones.
  The edit form of the project contains fields to choose the product versions, categories,
  licenses and plattforms.
- The add-on send message once a new project was added. It push a message too, once a project
  was submitted for publication. It send an email to the project contact address for every
  change in the workflow status of the project.
- The user could send a message to the author of a template via a mail. The mail form uses a
  honeypot field and honeypot widget for protecting it against robots. The contact data of 
  the author of the template will not be made public.
- The file extensions of the uploaded templates will be checked. It is possible to set the
  allowed file extensions distinct for the specific use case of the template center. They
  could be dynamically changed at any time.
- The add-on sends messages to the project contact email on every edit of the template
  center's product versions field (thus the contributors could potentially add this new
  product version to their project).


Examples
--------

This add-on can be seen in action at the following sites:
-


Documentation
-------------

Full documentation for end users isn't available yet, but will be available
soon in the "docs" folder


Translations
------------

This product has been translated into

- German


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


Support
-------

If you are having issues, please let us know.
Please create an issue in the project issue tracker (see above).


License
-------

The project is licensed under the GPLv2.
