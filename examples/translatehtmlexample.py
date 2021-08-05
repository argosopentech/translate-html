import argostranslate
from argostranslate import translate
from argostranslate.tags import translate_tags

import bs4
from bs4 import BeautifulSoup

import translatehtml
from translatehtml import *


# Requires Argos Translate installed languages
installed_languages = translate.get_installed_languages()
underlying_translation = installed_languages[0].get_translation(installed_languages[1])

html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

translated_soup = translate_html(underlying_translation, html_doc)

print(translated_soup)
