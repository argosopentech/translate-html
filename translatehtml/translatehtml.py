import bs4
from bs4 import BeautifulSoup
from bs4.element import NavigableString

import argostranslate
from argostranslate.tags import Tag, translate_tags

NON_TRANSLATEABLE_TAGS = [
    "address",
    "applet",
    "audio",
    "canvas",
    "code",
    "embed",
    "script",
    "style",
    "time",
    "video",
]


def itag_of_soup(soup):
    """Returns an argostranslate.tags.ITag tree from a BeautifulSoup object.

    Args:
        soup (bs4.element.Navigablestring or bs4.element.Tag): Beautiful Soup object

    Returns:
        argostranslate.tags.ITag: Argos Translate ITag tree
    """
    if isinstance(soup, bs4.element.NavigableString):
        return str(soup)
    translateable = soup.name not in NON_TRANSLATEABLE_TAGS
    to_return = Tag([itag_of_soup(content) for content in soup.contents], translateable)
    to_return.soup = soup
    return to_return


def soup_of_itag(itag):
    """Returns a BeautifulSoup object from an Argos Translate ITag.

    Args:
        itag (argostranslate.tags.ITag): ITag object to convert to Soup

    Returns:
        bs4.elements.BeautifulSoup: BeautifulSoup object
    """
    if type(itag) == str:
        return bs4.element.NavigableString(itag)
    soup = itag.soup
    soup.contents = [soup_of_itag(child) for child in itag.children]
    return soup


def translate_html(underlying_translation, html):
    """Translate HTML str.

    Args:
        underlying_translation (argostranslate.translate.ITranslation): Argos Translate Translation
        html (str): An HTML string

    Returns:
        str: Translated HTML string
    """
    soup = BeautifulSoup(html, "html.parser")
    itag = itag_of_soup(soup)
    translated_tag = translate_tags(underlying_translation, itag)
    translated_soup = soup_of_itag(translated_tag)
    return translated_soup
