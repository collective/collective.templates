# -*- coding: utf-8 -*-
from plone import api
from plone.restapi.services import Service
from plone.restapi.serializer.converters import json_compatible


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
