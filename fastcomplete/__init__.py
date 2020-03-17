import argcomplete
import os

from .parser_cache import save_cache, load_cache


# This class derives from CompletionFinder and allows caching its data to prevent multiple runs of the same script
class CachedCompletionFinder(argcomplete.CompletionFinder):
    def __call__(self, *args, **kwargs):
        parser_cache.save_cache(args, kwargs)
        return super().__call__(*args, **kwargs)


autocomplete = CachedCompletionFinder()
autocomplete.__doc__ = """ Use this to access fastcomplete. See :meth:`fastcomplete.CachedCompletionFinder.__call__()`. """

loaded_cache = parser_cache.load_cache()
if loaded_cache is not None:
    autocomplete(*loaded_cache)
