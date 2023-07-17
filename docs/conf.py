# Configuration file for the Sphinx documentation builder.
#
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------

project = 'HDL, Analog Devices'
copyright = '2023, Analog Devices Inc'
author = 'Analog Devices Inc'
release = 'v0.1'

# -- General configuration ---------------------------------------------------

import os, sys

sys.path.append(os.path.abspath("./extensions"))

extensions = [
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinxcontrib.bibtex",
    "sphinxcontrib.mermaid",
    "sphinxcontrib.wavedrom",
    "symbolator_sphinx",
    "git",
    "part",
    "dokuwiki",
    "datasheet"
]

templates_path = ['sources/template']

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Custom extensions configuraion -------------------------------------------

git_org_url = 'https://github.com/analogdevicesinc'
part_url = 'https://www.analog.com/products'
dokuwiki_url = 'https://wiki.analog.com'
datasheet_url = 'https://www.analog.com/media/en/technical-documentation/data-sheets/'

# -- todo configuration -------------------------------------------------------

todo_include_todos = True
todo_emit_warnings = True

# -- Symbolator configuration -------------------------------------------------

symbolator_cmd = '/usr/local/bin/symbolator' # Update with your installed location
symbolator_cmd_args = ['-t', '--scale=0.75']

# -- BibTeX configuration -----------------------------------------------------

bibtex_bibfiles = ['appendix/references.bib']

# -- Options for HTML output --------------------------------------------------

html_theme = 'furo'
html_static_path = ['sources']
source_suffix = '.rst'
html_css_files = ["custom.css"]
html_favicon = "sources/icon.svg"
