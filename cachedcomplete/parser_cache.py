'''
Cache for saving python objects based on source code hashes.
'''
from __future__ import print_function

import os
import pickle
import sys
import subprocess
from .main_script import MAIN_FILE_PATH, get_files_to_hash
from .main_script import exists as main_script_exists


CACHE_DIR = '/tmp/.cachedcomplete'
CACHE_FILE = os.path.join(CACHE_DIR, '{file}-{hash}')


def get_cache_filename():
    '''
    :return: the full path to the expected cache file.
    '''
    return CACHE_FILE.format(hash=_calc_hash(), file=os.path.basename(MAIN_FILE_PATH))


def save_cache(*args):
    '''
    :param args: The objects saved in the cache.
    :type args: Anything that can be saved using pickle.
    '''
    if not main_script_exists():
        print("warning: refusing to cache: cannot find the main script's file", file=sys.stderr)
        return

    if not os.path.isdir(CACHE_DIR):
        os.makedirs(CACHE_DIR)

    cache_file = get_cache_filename()
    if os.path.isfile(cache_file):
        return

    with open(cache_file, 'wb') as cache:
        pickle.dump(args, cache, protocol=pickle.HIGHEST_PROTOCOL)


def load_cache():
    '''
    :return:
        The objects that were loaded from the saved cache.
        ``None`` in case the cache is empty.
    '''
    if not main_script_exists():
        return

    cache_file = get_cache_filename()
    if not os.path.isfile(cache_file):
        return

    try:
        with open(cache_file, 'rb') as cache:
            return pickle.load(cache)
    except:
        # Delete the cache if we couldn't read it, so that next time
        # we complete there's a cache.
        os.unlink(cache_file)


def _calc_hash():
    '''
    Calculate the hash on all necessary files.

    :return: A string.
    '''
    files = ' '.join(get_files_to_hash())

    old_pwd = os.path.abspath(os.curdir)
    try:
        if MAIN_FILE_PATH is not None:
            os.chdir(os.path.dirname(MAIN_FILE_PATH))

        return subprocess.check_output(
            r"find {} -type f -\! -name '*.pyc' -print0 | sort -zu | xargs -0 cat | md5sum | awk '{{ print $1 }}'".format(files),
            shell=True, stderr=subprocess.DEVNULL).decode().strip()
    finally:
        os.chdir(old_pwd)
