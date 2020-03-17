# fastcomplete
Fast semi-static autocomplete for python

## Usage of custom subclasses of CompletionFinder
In order to use custom CompletionFinders with fastcomplete, 
a usage of the decorator cached_completion_finder is required.
### For example:
#### Using argcomplete:
```python
import argcomplete

class CustomCompletionFinder(argcomplete.CompletionFinder):
    ...

completion_finder = CustomCompletionFinder()
# Instead of argcomplete.autocomplete()
completion_finder()
```
#### Using fastcomplete:
```python
import argcomplete
import fastcomplete

@fastcomplete.cached_completion_finder
class CustomCompletionFinder(argcomplete.CompletionFinder):
    ...

completion_finder = CustomCompletionFinder()
# Instead of argcomplete.autocomplete()
completion_finder()
```
##### or
```python
import argcomplete
import fastcomplete

class CustomCompletionFinder(argcomplete.CompletionFinder):
    ...

completion_finder = fastcomplete.cached_completion_finder(CustomCompletionFinder)()
# Instead of argcomplete.autocomplete()
completion_finder()
```