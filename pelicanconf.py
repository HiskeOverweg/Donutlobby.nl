AUTHOR = "Hiske Overweg"
SITENAME = "De Donutlobby"
SITEURL = ""
THEME = "./theme"
PATH = "content"
PAGE_PATHS = ["pages"]
ARTICLE_PATHS = ["articles"]

DISPLAY_CATEGORIES_ON_MENU = False

TIMEZONE = "Europe/Amsterdam"

DEFAULT_LANG = "nl"

PLUGIN_PATHS = ["./plugins"]
PLUGINS = ["i18n_subsites"]


I18N_SUBSITES = {
    "en": {
        "SITENAME": "Donutlobby",
        "LOCALE": "en_US",  # This is somewhat redundant with DATE_FORMATS, but IMHO more convenient
    },
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Page order
PAGE_ORDER_BY = "order"

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
