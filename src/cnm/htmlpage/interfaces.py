# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from cnm.htmlpage import _
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class ICnmHtmlpageLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IHTMLPage(Interface):

    title = schema.TextLine(
        title=_(u'Title'),
        required=True,
    )

    description = schema.Text(
        title=_(u'Description'),
        required=False,
    )

    html_content = schema.Text(
        title=_(u'HTML Content'),
        description=_(u"Add all HTML, CSS, and JS to this field"),
        required=True,
    )
