import os
import sys

# Setting up the root folder
sys.path.insert(0, os.path.abspath('..'))

project = 'datewise'
author = 'Sebastian Gontkovic'
copyright = 'Sebastian Gontkovic, 2024, Bratislava'

extensions = [
    'recommonmark',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode'
]

html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
