import os
import sys

from os import path
from typing import Dict, List, Optional, Tuple


DAYS_ARG = '-d'     # type: str
YEAR_ARG = '-y'     # type: str
LANG_ARG = '-l'     # type: str

TEMPLATE_PATH = '.\\templates\\template.*'    # type: str

SUPPORTED_LANGUAGES = {
    'py': ('Python', 'main'),
    'cpp': ('C++', 'main'),
    'cs': ('C#', 'Program'),
}   # type: Dict[str, Tuple[str, str]]


def main():
    args = sys.argv     # type: List[str]
    day = None          # type: Optional[str]
    year = None         # type: Optional[str]
    language = None     # type: Optional[str]

    if len(args) != 7:
        print('Invalid number of command line arguments! Use \'-y\', \'-d\' and \'-l\'')
        return

    if DAYS_ARG not in args:
        print('Missing %s command line argument!' % DAYS_ARG)
        return
    else:
        day = args[args.index(DAYS_ARG) + 1]

        if len(day) == 1:
            day = '0' + day

    if YEAR_ARG not in args:
        print('Missing %s command line argument!' % YEAR_ARG)
        return
    else:
        year = args[args.index(YEAR_ARG) + 1]

        if int(year) < 2015:
            print('Invalid year!')
            return

    if LANG_ARG not in args:
        print('Missing %s command line argument!' % LANG_ARG)
        return
    else:
        language = args[args.index(LANG_ARG) + 1]

        if language not in SUPPORTED_LANGUAGES:
            print('Unsupported language! Supported languages: ', SUPPORTED_LANGUAGES.values())
            return

    current_language = SUPPORTED_LANGUAGES[language]
    new_dir = os.path.dirname(os.path.abspath(__file__)) + '\\' + year

    if not path.exists(new_dir):
        os.mkdir(new_dir)

    new_dir += '\\Day_' + day

    if not path.exists(new_dir):
        os.mkdir(new_dir)

    new_dir += '\\' + current_language[0] + '\\'

    if not path.exists(new_dir):
        os.mkdir(new_dir)

    new_path = new_dir + current_language[1] + '.' + language

    with open(new_path, 'w') as new_file:
        with open(TEMPLATE_PATH.replace('*', language), 'r') as template_file:
            for line in template_file.readlines():
                new_file.write(line)


if __name__ == '__main__':
    main()
