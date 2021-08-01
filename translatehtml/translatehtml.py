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

