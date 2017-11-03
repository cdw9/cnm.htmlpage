# -*- coding: utf-8 -*-
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from cnm.htmlpage.interfaces import IHTMLPage
from cnm.htmlpage.testing import CNM_HTMLPAGE_INTEGRATION_TESTING  # noqa
from zope.component import createObject
from zope.component import queryUtility

import unittest


class HTMLPageIntegrationTest(unittest.TestCase):

    layer = CNM_HTMLPAGE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='HTMLPage')
        schema = fti.lookupSchema()
        self.assertEqual(IHTMLPage, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='HTMLPage')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='HTMLPage')
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(IHTMLPage.providedBy(obj))

    def test_adding(self):
        obj = api.content.create(
            container=self.portal,
            type='HTMLPage',
            id='HTMLPage',
        )
        self.assertTrue(IHTMLPage.providedBy(obj))
