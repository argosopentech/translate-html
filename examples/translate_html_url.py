import argostranslate
from argostranslate import translate
from argostranslate.tags import translate_tags
import argparse

import bs4
from bs4 import BeautifulSoup

import translatehtml
from translatehtml import *

import urllib

# Requires Argos Translate installed languages
installed_languages = translate.get_installed_languages()

parser = argparse.ArgumentParser(description='Translate HTML pages or files')
parser.add_argument('url', type=str, metavar="<URL | file path>",
                    help='Path to local file or URL (e.g. https://google.com or /home/user/test.html)')
parser.add_argument('from', type=str, metavar="<lang from>",
                    help="Translate from language", default="en")
parser.add_argument('to', type=str, metavar="<lang to>",
                    help="Translate to language", default="es")
args = vars(parser.parse_args())

try:
    from_lang = [il for il in installed_languages if il.code == args['from']][0]
except IndexError:
    print(args['from'] + " is not available")
    exit(1)

try:
    to_lang = [il for il in installed_languages if il.code == args['to']][0]
except IndexError:
    print(args['to'] + " is not available")
    exit(1)

underlying_translation = from_lang.get_translation(to_lang)

if args['url'].lower().startswith("http://") or args['url'].lower().startswith("https://"):
    f = urllib.request.urlopen(args['url'])
else:
    f = open(args['url'])

html_doc = f.read()

translated_soup = translate_html(underlying_translation, html_doc)
print(translated_soup)
