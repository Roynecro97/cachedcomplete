'''
Gets values fron special comments in the first 1024 bytes of the main script.
'''
import os
import re
import sys
import shlex

from itertools import chain


SEARCH_RANGE = 1024
INFO_PREFIX = 'CACHEDCOMPLETE_'
FILES_TO_HASH_INFO = INFO_PREFIX + r'HASH:\s*(?P<files>.*)$'

# Path to the main script
MAIN_FILE_PATH = os.path.abspath(sys.argv[0])


def _get_info_list(expr):
    '''
    :return: an iterable of all items from the main script (not an actual list).
    '''
    with open(MAIN_FILE_PATH) as main_file:
        content = main_file.read(SEARCH_RANGE)
    return chain(*(shlex.split(match.group('files')) for match in re.finditer(expr, content, re.M)))


def _expand(filename):
    return shlex.quote(os.path.abspath(os.path.expanduser(os.path.expandvars(filename))))


def get_files_to_hash():
    return chain([MAIN_FILE_PATH, os.path.dirname(__file__)], (_expand(filename) for filename in _get_info_list(FILES_TO_HASH_INFO)))
