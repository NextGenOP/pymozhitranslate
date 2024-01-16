# Pymozhitranslate

This project is in progress

# Install
```
pip install git+https://github.com/NextGenOP/pymozhitranslate
```

# Usage

## CLI

```shell
$ mozhitranslate -h

Simple translator tool.


Options:
  -h, --help             Display this message
  -e --engine            Translator engine to use
  -s, --source           Source Language to translate
  -t, --target           Target Language to translate
  -txt, --text           Text to translate
  -ll, --list-languages  List Languages support
  -f, --file             Path file .txt to translate
  -o, --output           Output file translation result

$ mozhitranslate -s auto -t id -txt "How are You ?"
 Apa kabar ?

$ mozhitranslate -s auto -t id -txt "How are You ?" -o output.txt
 Translation result saved in output.txt

$ mozhitranslate -s auto -t id -f input.txt -o output.txt
 Translation result saved in output.txt
```

## Python

### List languages

```python
from pymozhitranslate import Translator
trans = Translator()
list_languages = trans.languages()
print(list_languages)
```

**Output:**

```
{'Detect': 'auto', 'Afrikaans': 'af', 'Albanian': 'sq', 'Amharic': 'am', 'Arabic': 'ar', 'Armenian': 'hy', 'Azerbaijani': 'az', 'Basque': 'eu', 'Belarusian': 'be', 'Bengali': 'bn', 'Bosnian': 'bs', 'Bulgarian': 'bg', 'Catalan': 'ca', 'Cebuano': 'ceb', 'Chichewa': 'ny', 'Chinese': 'zh', 'Chinese (Traditional)': 'zh_HANT', 'Corsican': 'co', 'Croatian': 'hr', 'Czech': 'cs', 'Danish': 'da', 'Dutch': 'nl', 'English': 'en', 'Esperanto': 'eo', 'Estonian': 'et', 'Filipino': 'tl', 'Finnish': 'fi', 'French': 'fr', 'Frisian': 'fy', 'Galician': 'gl', 'Georgian': 'ka', 'German': 'de', 'Greek': 'el', 'Gujarati': 'gu', 'Haitian Creole': 'ht', 'Hausa': 'ha', 'Hawaiian': 'haw', 'Hebrew': 'iw', 'Hindi': 'hi', 'Hmong': 'hmn', 'Hungarian': 'hu', 'Icelandic': 'is', 'Igbo': 'ig', 'Indonesian': 'id', 'Irish': 'ga', 'Italian': 'it', 'Japanese': 'ja', 'Javanese': 'jw', 'Kannada': 'kn', 'Kazakh': 'kk', 'Khmer': 'km', 'Kinyarwanda': 'rw', 'Korean': 'ko', 'Kurdish (Kurmanji)': 'ku', 'Kyrgyz': 'ky', 'Lao': 'lo', 'Latin': 'la', 'Latvian': 'lv', 'Lithuanian': 'lt', 'Luxembourgish': 'lb', 'Macedonian': 'mk', 'Malagasy': 'mg', 'Malay': 'ms', 'Malayalam': 'ml', 'Maltese': 'mt', 'Maori': 'mi', 'Marathi': 'mr', 'Mongolian': 'mn', 'Myanmar (Burmese)': 'my', 'Nepali': 'ne', 'Norwegian': 'no', 'Odia (Oriya)': 'or', 'Pashto': 'ps', 'Persian': 'fa', 'Polish': 'pl', 'Portuguese': 'pt', 'Punjabi': 'pa', 'Romanian': 'ro', 'Russian': 'ru', 'Samoan': 'sm', 'Scots Gaelic': 'gd', 'Serbian': 'sr', 'Sesotho': 'st', 'Shona': 'sn', 'Sindhi': 'sd', 'Sinhala': 'si', 'Slovak': 'sk', 'Slovenian': 'sl', 'Somali': 'so', 'Spanish': 'es', 'Sundanese': 'su', 'Swahili': 'sw', 'Swedish': 'sv', 'Tajik': 'tg', 'Tamil': 'ta', 'Tatar': 'tt', 'Telugu': 'te', 'Thai': 'th', 'Turkish': 'tr', 'Turkmen': 'tk', 'Ukrainian': 'uk', 'Urdu': 'ur', 'Uyghur': 'ug', 'Uzbek': 'uz', 'Vietnamese': 'vi', 'Welsh': 'cy', 'Xhosa': 'xh', 'Yiddish': 'yi', 'Yoruba': 'yo', 'Zulu': 'zu'}
```

### Translate

```python
from pymozhitranslate import Translator
trans = Translator()
txt = "Halo apa kabar ?"
translate = trans.translate("auto", "en", txt)
print(translate)
```

**Output**:

```
Hello, how are you ?
```

#### Custom URL

```
from pymozhitranslate import Translator
trans = Translator(url=["https://example.org"])
txt = "Halo apa kabar ?"
translate = trans.translate("auto", "en", txt)
print(translate)
```

#### Custom engine and URL

```
from pymozhitranslate import Translator
trans = Translator(url=["https://example.org"], engine="duckduckgo")
txt = "Halo apa kabar ?"
translate = trans.translate("auto", "en", txt)
print(translate)
```

This project is fork from [pylingva](https://gitlab.com/nesstero/pylingva)
