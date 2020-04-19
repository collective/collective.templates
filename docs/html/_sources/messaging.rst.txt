Messaging
#########

The collective.template Plone add-on use some of the Plone messaging
implementations to create messages to the site admin, reviewers and the
owner / creator of teplate projects.

Messages To The Site-Admininstrator / Administrator
***************************************************

- The site-administrator / admiinstrator get an e-mail once a new
  template project have been added to the template center.
- If the project owner submit her / his project for publication, the
  site-administrator / administrator get an e-mail about this event.

If the form field 'contactForCenter' in the templaten center contains an
e-mail address the above messages will be send to this address. Otherwise
the e-mail goes to the e-mail address of the Plone site.



Messages To The Project Owner
*****************************

- Once a workflow status of his project(s) change the project owner will get a
  message (e-mail) which inform her / him about this new status.
- Once the site-administrator / administrator of the Plone site adds a new
  product version to the form field 'Available Versions' the owner of a
  project will get an e-mail to inform her / him about this event. The message
  ask the owner to update the versions list of his
  project(s).






