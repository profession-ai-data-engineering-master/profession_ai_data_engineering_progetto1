"""Configurazione di Sphinx per la documentazione API del progetto."""

from importlib.metadata import version as _version

project = "Gestore delle Spese Domestiche"
author = "Federico Vita"
copyright = "2026, Federico Vita"
release = _version("gestore-spese")

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

language = "it"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# Le docstring usano i campi reStructuredText (:param:, :return:, ...).
autodoc_member_order = "bysource"
autodoc_typehints = "description"
add_module_names = False

html_theme = "furo"
