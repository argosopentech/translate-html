import bs4
from bs4 import *

import argostranslate
from argostranslate.tags import *
from argostranslate import package, translate


class HTMLTag(Tag):
    pass


def itag_of_soup(soup):
    if isinstance(soup, bs4.element.NavigableString):
        return str(soup)
    elif len(soup.contents) == 0:
        to_return = HTMLTag(list())
    elif len(soup.contents) == 1 and isinstance(
        soup.contents[0], bs4.element.NavigableString
    ):
        to_return = HTMLTag([str(soup.contents[0])])
    else:
        to_return = HTMLTag([itag_of_soup(content) for content in soup.contents])
    to_return.soup = soup
    return to_return


def soup_of_itag(itag):
    if type(itag) == str:
        return bs4.element.NavigableString(itag)
    soup = itag.soup
    if is_tag_literal(itag):
        soup.contents = [bs4.element.NavigableString(itag.text())]
    elif isinstance(itag, argostranslate.tags.Tag):
        soup.contents = [soup_of_itag(content) for content in itag.children()]
    return soup


installed_languages = translate.get_installed_languages()
translation_en_es = installed_languages[0].get_translation(installed_languages[1])

read_file = False

if not read_file:
    html_doc = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title"><b>The Dormouse's story</b></p>

    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>

    <p class="story">...</p>
    """

    soup = BeautifulSoup(html_doc, "html.parser")
else:
    soup = BeautifulSoup(open("index.html"), "html.parser")


htmltag = itag_of_soup(soup)


translated_tags = translate_tags(translation_en_es, htmltag)


translated_soup = soup_of_itag(translated_tags)

print(translated_soup)
