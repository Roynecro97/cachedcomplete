#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK
# CACHEDCOMPLETE_HASH: ~/.bashrc ~/.bash_aliases
# CACHEDCOMPLETE_HASH: ~/.bash_logout ./i-dont-exist
# CACHEDCOMPLETE_HASH: "./damn space"

import argparse
import cachedcomplete

from imported_module import json_file, completer

import os
os.write(0, b'\nRunning custom_type_test.py\n')

def _main():
    p = argparse.ArgumentParser()
    p.add_argument('-f', '--foo').completer = completer
    p.add_argument('settings', type=json_file)
    cachedcomplete.autocomplete(p)
    print(p.parse_args())

if __name__ == '__main__':
    _main()
