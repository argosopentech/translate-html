import bs4
from bs4.element import NavigableString

import argostranslate
from argostranslate.tags import Tag, translate_tags


def itag_of_soup(soup):
    if isinstance(soup, bs4.element.NavigableString):
        return str(soup)
    to_return = Tag([itag_of_soup(content) for content in soup.contents])
    to_return.soup = soup
    return to_return


def soup_of_itag(itag):
    if type(itag) == str:
        return bs4.element.NavigableString(itag)
    soup = itag.soup
    soup.contents = [soup_of_itag(child) for child in itag.children]
    return soup


def translate_html(underlying_translation, html):
    soup = BeautifulSoup(html, "html.parser")
    itag = itag_of_soup(soup)
    translated_tag = translate_tags(underlying_translation, itag)
    translated_soup = soup_of_itag(translated_tag)
    return translated_soup
