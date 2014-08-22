#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Joe Edwards'
SITENAME = 'Rice Microbiome'
SITEURL = ''#'http://ricemicrobiome.github.io/'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

STATIC_PATHS = [
    'images',
    'extras'
]

# What to do with output directory when updating
DELETE_OUTPUT_DIRECTORY = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Sundaresan Lab', 'http://sundarlab.ucdavis.edu'),
         ('Eisen Lab', 'http://phylogenomics.wordpress.com/'),
         ('UC Davis', 'http://www.ucdavis.edu'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "pelican-themes/RMBCustom"

TAG_FEED_ATOM = "feeds/tag_%s.atom.xml"

EXTRA_PATH_METADATA = {
    'extras/robots.txt': {'path': 'robots.txt'},
    'extras/favicon.ico': {'path': 'favicon.ico'},
}

# Publishing Extras
#GOOGLE_ANALYTICS = 'UA-54046198-1'
#DISQUS_SITENAME = "ricemicrobiome"


