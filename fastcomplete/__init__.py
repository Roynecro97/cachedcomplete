import argcomplete

from functools import wraps

from .parser_cache import save_cache, load_cache

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

    @wraps(completion_finder_cls, updated=())
    class CachedCompletionFinder(completion_finder_cls):
        def __call__(self, argument_parser, *args, **kwargs):
            argument_parser.register('type', None, identity)
            parser_cache.save_cache(argument_parser, args, kwargs)
            return super().__call__(argument_parser, *args, **kwargs)
    
    return CachedCompletionFinder


autocomplete = cached_complation_finder(argcomplete.CompletionFinder)()
autocomplete.__doc__ = argcomplete.autocomplete.__doc__

loaded_cache = parser_cache.load_cache()
if loaded_cache is not None:
    parser, args, kwargs = loaded_cache
    autocomplete(parser, *args, **kwargs)
