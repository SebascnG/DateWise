# -- Path setup ----------------------------------------
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# -- Project information -------------------------------
project = 'datewise'
copyright = '2024, Sebastian Gontkovic'
author = 'Sebastian Gontkovic'

# -- General configuration -----------------------------
extensions = [
    'recommonmark',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'English'

# -- Options for HTML output ---------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']