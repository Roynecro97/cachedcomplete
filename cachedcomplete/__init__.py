import argcomplete

from functools import wraps, WRAPPER_ASSIGNMENTS

from .parser_cache import save_cache, load_cache

if argcomplete.USING_PYTHON2:
    # Don't override __doc__ with wraps because it's read-only in python2
    __CLASS_WRAPPER_ASSIGNMENTS = tuple(filter(lambda attr: attr != '__doc__', WRAPPER_ASSIGNMENTS))

    _ARGPARSE_LOCAL_IDENTITY_NAME = 'identity'
else:
    __CLASS_WRAPPER_ASSIGNMENTS = WRAPPER_ASSIGNMENTS

    _ARGPARSE_LOCAL_IDENTITY_NAME = 'ArgumentParser.__init__.<locals>.identity'

def identity(string):
    '''
    identity function to path problems with argparse.
    '''
    return string

def cached_complation_finder(completion_finder_cls):
    '''
    This decorator wraps argcomplete.CompletionFinder and adds the cache save logic to its __call__
    '''
    if not issubclass(completion_finder_cls, argcomplete.CompletionFinder):
        raise TypeError("cached_completion_finder can only be used on classes that derive from CompletionFinder")

    @wraps(completion_finder_cls, assigned=__CLASS_WRAPPER_ASSIGNMENTS, updated=())
    class CachedCompletionFinder(completion_finder_cls):
        @staticmethod
        def __fix_default_type(argument_parser):
            '''
            Fix the default un-pickle-able argument type.
            '''
            if _ARGPARSE_LOCAL_IDENTITY_NAME in repr(argument_parser._registry_get('type', None, default='')):
                argument_parser.register('type', None, identity)

            if argument_parser._subparsers is not None:
                for group_action in argument_parser._subparsers._group_actions:
                    for parser in group_action.choices.values():
                        CachedCompletionFinder.__fix_default_type(parser)

        def __call__(self, argument_parser, *args, **kwargs):
            CachedCompletionFinder.__fix_default_type(argument_parser)
            save_cache(argument_parser, args, kwargs)
            return super(CachedCompletionFinder, self).__call__(argument_parser, *args, **kwargs)

    return CachedCompletionFinder


autocomplete = cached_complation_finder(argcomplete.CompletionFinder)()
autocomplete.__doc__ = argcomplete.autocomplete.__doc__

loaded_cache = load_cache()
if loaded_cache is not None:
    parser, args, kwargs = loaded_cache
    autocomplete(parser, *args, **kwargs)
