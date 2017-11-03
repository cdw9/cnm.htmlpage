# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from cnm.htmlpage.testing import CNM_HTMLPAGE_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that cnm.htmlpage is properly installed."""

    layer = CNM_HTMLPAGE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if cnm.htmlpage is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'cnm.htmlpage'))

    def test_browserlayer(self):
        """Test that ICnmHtmlpageLayer is registered."""
        from cnm.htmlpage.interfaces import (
            ICnmHtmlpageLayer)
        from plone.browserlayer import utils
        self.assertIn(ICnmHtmlpageLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = CNM_HTMLPAGE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['cnm.htmlpage'])

    def test_product_uninstalled(self):
        """Test if cnm.htmlpage is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'cnm.htmlpage'))

    def test_browserlayer_removed(self):
        """Test that ICnmHtmlpageLayer is removed."""
        from cnm.htmlpage.interfaces import \
            ICnmHtmlpageLayer
        from plone.browserlayer import utils
        self.assertNotIn(ICnmHtmlpageLayer, utils.registered_layers())
