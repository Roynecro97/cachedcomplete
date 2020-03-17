import argcomplete
import os


class FastcompleteCompletionFinder(argcomplete.CompletionFinder):
    def __call__(self, *args, **kwargs):
        return super().__call__(*args, **kwargs)


autocomplete = FastcompleteCompletionFinder()
autocomplete.__doc__ = """ Use this to access fastcomplete. See :meth:`fastcomplete.FastcompleteCompletionFinder.__call__()`. """
