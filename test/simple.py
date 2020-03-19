#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK
# CACHEDCOMPLETE_HASH: ~/.bashrc ~/.bash_aliases
# CACHEDCOMPLETE_HASH: ~/.bash_logout ./i-dont-exist
# CACHEDCOMPLETE_HASH: "./damn space"

import argparse
import cachedcomplete
import json

import os
os.write(0, b'test\n')

def _main():
    p = argparse.ArgumentParser()
    p.add_argument('-f', '--foo')
    cachedcomplete.autocomplete(p)
    print(p.parse_args())

if __name__ == '__main__':
    _main()
