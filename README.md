# translate-html
Translate HTML using [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/) and [Argos Translate](https://github.com/argosopentech/argos-translate)

## Install
```
pip install translatehtml
```

## [Example](examples/)
```
import argostranslate.package, argostranslate.translate
import translatehtml

from_code = "es"
to_code = "en"

html_doc = """<div><h1>Perro</h1></div>"""

# Download and install Argos Translate package
available_packages = argostranslate.package.get_available_packages()
available_package = list(
    filter(
        lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
    )
)[0]
download_path = available_package.download()
argostranslate.package.install_from_path(download_path)

# Translate
installed_languages = argostranslate.translate.get_installed_languages()
from_lang = list(filter(lambda x: x.code == from_code, installed_languages))[0]
to_lang = list(filter(lambda x: x.code == to_code, installed_languages))[0]

translation = from_lang.get_translation(to_lang)

translated_soup = translatehtml.translate_html(translation, html_doc)

print(translated_soup)

```

## Links
- [OpenNMT Forum](https://forum.opennmt.net/t/suggestions-for-translating-xml/4409)
- [GitHub Discussion](https://github.com/argosopentech/argos-translate/discussions/158)
