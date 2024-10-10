# -*- coding: utf-8 -*-

# auxilium
# --------
# A Python project for an automated test and deploy toolkit - 100%
# reusable.
#
# Author:   sonntagsgesicht
# Version:  0.1.4, copyright Sunday, 11 October 2020
# Website:  https://github.com/sonntagsgesicht/auxilium
# License:  Apache License 2.0 (see LICENSE file)

import os
import sys

sys.path.append('../..')

# -- Import project pkg ---------------------------------------------------

pos = -5 if 'readthedocs' in __file__ else -3  # hack for readthedocs.org
pkg_path = __file__.split(os.sep)[:pos]
sys.path.append(os.sep.join(pkg_path))
pkg = __import__(pkg_path[-1])

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.

needs_sphinx = '1.8'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_pytype_substitution',
    'sphinx_math_dollar',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.inheritance_diagram',
]

# Extend extensions by project theme
if pkg.__theme__ and pkg.__theme__.replace('-', '_') not in extensions:
    extensions.append(pkg.__theme__.replace('-', '_'))

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = pkg.__name__.capitalize()
copyright = pkg.__author__
author = pkg.__email__

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = pkg.__version__
# The full version, including alpha/beta/rc tags.
release = pkg.__version__ + ' [' + pkg.__dev_status__ + ']'
# today as date of release
today = pkg.__date__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `to_do` and `to_do_List` produce output, else they produce nothing.
todo_include_todos = False

# A boolean that decides whether module names are prepended to all object
# names.
add_module_names = True

# -- Options for HTML output ----------------------------------------------

if pkg.__theme__:
    html_theme = pkg.__theme__.replace('-', '_')
# html_logo = 'logo.png'
# html_theme_options = {}
# html_static_path = ['_static']


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
}
# latex_logo = 'logo.png'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [(
    master_doc,
    pkg.__name__ + '.tex',
    pkg.__name__.capitalize() + ' Documentation',
    pkg.__author__,
    'manual'
), ]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).

man_pages = [(
    master_doc,
    pkg.__name__,
    pkg.__name__.capitalize() + ' Documentation',
    [pkg.__author__],
    1)
]


# -- Options for autodoc extension -----------------------------------------

autodoc_default_options = {
    'show-inheritance': 1,
    'inherit_docstrings': True,
    'member-order': 'bysource',
    'members': True,  # 'var1, var2',
    'undoc-members': True,
    'private-members': False,
    'inherited-members': False,
    # 'imported-members': False,
    # 'special-members': '__call__',
    # 'exclude-members': '__weakref__',
    # 'autosummary': True,
    # 'ignore-module-all':
    # 'class-doc-from':
}
# This value selects what content will be inserted into the main body of an
# autoclass directive. (autodoc)
# "class" Only the class’ docstring is inserted.
# "init" Only the __init__ method’s docstring is inserted.
# "both" Both the class’ and the __init__ method’s docstring are inserted.
autoclass_content = 'init'

# This value selects how the signature will be displayed for the class defined
# by autoclass directive. (autodoc)
# "mixed" Display the signature with the class name.
# "separated" Display the signature as a method.
autodoc_class_signature = "mixed"

# -- Config for math-dollar extension (mathjax) ----------------------------

mathjax3_config = {
    'tex2jax': {
        'inlineMath': [["\\(", "\\)"]],
        'displayMath': [["\\[", "\\]"]],
    },
}

# -- Config for pytype_substitution extension ------------------------------

pytype_substitutions = pkg,  # package, module or class to reference to
pytype_buildins = False  # not implemented in v0.1
pytype_short_ref = True  # drop module from reference (if it does not conflict)
pytype_match_pattern = ''  # regex to filter entities to ref to
pytype_exclude_pattern = ''  # regex to exclude entities to ref to
