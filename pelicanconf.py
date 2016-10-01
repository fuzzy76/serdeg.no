#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'SerDeg.no'
SITENAME = 'SerDeg.no'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Oslo'
DEFAULT_DATE_FORMAT = '%A %-d. %B %Y'

DEFAULT_LANG = 'no_NO.UTF-8'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['articles']
STATIC_PATHS = ['images','extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

DEFAULT_DATE = 'fs'
PLUGIN_PATHS = ['plugins']
PLUGINS = []
MD_EXTENSIONS = ["codehilite(css_class=highlight)", "extra", "toc"]

TYPOGRIFY = True
THEME = 'theme'

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = '{category}/{slug}/'
PAGE_SAVE_AS = '{category}/{slug}/index.html'
#CATEGORY_URL = '{slug}'
#CATEGORY_SAVE_AS = '{slug}/index.html'
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
TAG_SAVE_AS = ''
INDEX_SAVE_AS = 'nyheter/index.html'

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = []
