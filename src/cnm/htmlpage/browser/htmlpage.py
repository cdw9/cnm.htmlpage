from plone import api
from Products.Five.browser import BrowserView


class HTMLPage(BrowserView):
    """ View class for the HTMLPage View
    """

    def __init__(self, context, request=None):
        self.context = context
        self.request = request

    def is_admin(self):
        # return True if user is Manager or Site Admin
        membership = api.portal.get_tool("portal_membership")
        # if not membership.isAnonymousUser():
        user = membership.getAuthenticatedMember()
        roles = user.getRolesInContext(self.context)
        return 'Manager' in roles or 'Site Administrator' in roles
