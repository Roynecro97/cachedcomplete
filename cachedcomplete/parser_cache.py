'''
Cache for saving python objects based on source code hashes.
'''
import os
import subprocess
from argcomplete import USING_PYTHON2
from .main_script import MAIN_FILE_PATH, get_files_to_hash

# Use the optimized C version for pickle
if USING_PYTHON2:
    import cPickle as pickle
else:
    import pickle


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
    cache_file = get_cache_filename()
    if not os.path.isfile(cache_file):
        return

    try:
        with open(cache_file, 'rb') as cache:
            return pickle.load(cache)
    except:
        # Delete the cahe if we couldn't read it, so that next time
        # we complete there's a cache.
        os.unlink(cache_file)


def _calc_hash():
    '''
    Calculate the hash on all necessary files.

    :return: A string.
    '''
    if USING_PYTHON2:
        devnull = open(os.devnull, 'w')
    else:
        devnull = subprocess.DEVNULL

    files = ' '.join(get_files_to_hash())

    try:
        return subprocess.check_output(
            r"find {} -type f -\! -name '*.pyc' -print0 | xargs -0 cat | md5sum | awk '{{ print $1 }}'".format(files),
            shell=True, stderr=devnull).decode().strip()
    finally:
        if USING_PYTHON2:
            devnull.close()
