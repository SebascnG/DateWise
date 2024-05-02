import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'datewise'
copyright = '2024, Sebastian Gontkovic'
author = 'Sebastian Gontkovic'

extensions = [
    'recommonmark',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode'
]

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
