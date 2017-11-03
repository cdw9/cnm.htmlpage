# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import cnm.htmlpage


class CnmHtmlpageLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=cnm.htmlpage)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'cnm.htmlpage:default')


CNM_HTMLPAGE_FIXTURE = CnmHtmlpageLayer()


CNM_HTMLPAGE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(CNM_HTMLPAGE_FIXTURE,),
    name='CnmHtmlpageLayer:IntegrationTesting'
)


CNM_HTMLPAGE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(CNM_HTMLPAGE_FIXTURE,),
    name='CnmHtmlpageLayer:FunctionalTesting'
)


CNM_HTMLPAGE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        CNM_HTMLPAGE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CnmHtmlpageLayer:AcceptanceTesting'
)
