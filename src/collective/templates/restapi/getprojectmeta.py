# -*- coding: utf-8 -*-
from plone import api
from plone.restapi.serializer.converters import json_compatible
from plone.restapi.services import Service


class Projectcategories(Service):
    def reply(self):
        catalog = api.portal.get_tool(name='portal_catalog')
        path = '/'.join(self.context.getPhysicalPath())
        idx_data = catalog.getIndexDataForUID(path)
        category = idx_data.get('getCategories')
        return json_compatible(category)


class Projectlicenses(Service):
    def reply(self):
        catalog = api.portal.get_tool(name='portal_catalog')
        path = '/'.join(self.context.getPhysicalPath())
        idx_data = catalog.getIndexDataForUID(path)
        licenses = idx_data.get('releaseLicense')
        return json_compatible(licenses)


class Releasecompatibility(Service):
    def reply(self):
        catalog = api.portal.get_tool(name='portal_catalog')
        path = '/'.join(self.context.getPhysicalPath())
        idx_data = catalog.getIndexDataForUID(path)
        compatibility = idx_data.get('getCompatibility')
        return json_compatible(compatibility)


class Emailpublic(Service):
    def reply(self):
        catalog = api.portal.get_tool(name='portal_catalog')
        path = '/'.join(self.context.getPhysicalPath())
        idx_data = catalog.getIndexDataForUID(path)
        public_email = idx_data.get('publicemail')
        return json_compatible(public_email)


class Namepublic(Service):
    def reply(self):
        catalog = api.portal.get_tool(name='portal_catalog')
        path = '/'.join(self.context.getPhysicalPath())
        idx_data = catalog.getIndexDataForUID(path)
        public_name = idx_data.get('publicname')
        return json_compatible(public_name)
