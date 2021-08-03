import bs4
from bs4.element import NavigableString

import argostranslate
from argostranslate.tags import Tag


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
