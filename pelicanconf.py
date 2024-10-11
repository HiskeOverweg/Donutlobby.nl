AUTHOR = "Hiske Overweg"
SITENAME = "De Donutlobby"
SITEURL = ""
THEME = "./theme"
PATH = "content"
PAGE_PATHS = ["pages"]
ARTICLE_PATHS = ["articles"]

MENUITEMS = [("Blog", "/category/articles.html")]
DISPLAY_CATEGORIES_ON_MENU = False

TIMEZONE = "Europe/Amsterdam"

DEFAULT_LANG = "nl"

PLUGIN_PATHS = ["/Users/hiske/repos/pelican-plugins"]
PLUGINS = ["i18n_subsites"]


I18N_SUBSITES = {
        'en': {
            'SITENAME': 'Donutlobby',
            'LOCALE': 'en_US',            #This is somewhat redundant with DATE_FORMATS, but IMHO more convenient
            },
        }


languages_lookup = {
    'en': 'English',
    'nl': 'Nederlands',
    }


def lookup_lang_name(lang_code):
    return languages_lookup[lang_code]


def my_ordered_items(dict):
    items = list(dict.items())
    # swap first and last using tuple unpacking
    items[0], items[-1] = items[-1], items[0]
    return items

JINJA_ENVIRONMENT = {
        'extensions': ['jinja2.ext.i18n'],
    }

JINJA_FILTERS = {
    'lookup_lang_name': lookup_lang_name,
    'my_ordered_items': my_ordered_items,
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
