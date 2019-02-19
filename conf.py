# -*- coding: utf-8 -*-

import sys, os
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = u'Meter'
copyright = u'2019, Phil Grunewald and Marina Diakonova'
author = u'Phil Grunewald and Marina Diakonova'

# The short X.Y version
version = u'1'
# The full version, including alpha/beta/rc tags
release = u'v.1'


# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
]

master_doc = 'index'
source_suffix = '.rst'
language = None

exclude_patterns = [u'html', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#

html_theme = 'alabaster'#"classic"
html_theme_options = {
    "github_repo":      "alabaster",
    "head_font_family": "Merriweather",
    "fixed_sidebar":    "False",
    "show_related":     "True"
}

html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
html_logo = "images/meter_logo.png"
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'Meterdoc'


# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True
