# cachedcomplete
Fast semi-static autocomplete for python

## Normal Usage
The normal usage is the same as in argcomplete, only changing the import from argcomplete to cachedcomplete
_Note: The usage of PYTHON_ARGCOMPLETE_OK stays the same as in argcomplete_
### For Example:
#### Using argcomplete:
```python
# PYTHON_ARGCOMPLETE_OK
import argcomplete

# ...

argcomplete.autocomplete()
```
#### Using cachedcomplete:
```python
# PYTHON_ARGCOMPLETE_OK
import cachedcomplete

# ...

cachedcomplete.autocomplete()
```

## Usage of custom subclasses of CompletionFinder
In order to use custom CompletionFinders with cachedcomplete, 
a usage of the decorator cached_completion_finder is required.
### For example:
#### Using argcomplete:
```python
import argcomplete

class CustomCompletionFinder(argcomplete.CompletionFinder):
    # ...

completion_finder = CustomCompletionFinder()
# Instead of argcomplete.autocomplete()
completion_finder()
```
#### Using cachedcomplete:
```python
import argcomplete
import cachedcomplete

@cachedcomplete.cached_completion_finder
class CustomCompletionFinder(argcomplete.CompletionFinder):
    # ...

completion_finder = CustomCompletionFinder()
# Instead of argcomplete.autocomplete()
completion_finder()
```
##### or
```python
import argcomplete
import cachedcomplete

class CustomCompletionFinder(argcomplete.CompletionFinder):
    # ...

completion_finder = cachedcomplete.cached_completion_finder(CustomCompletionFinder)()
# Instead of argcomplete.autocomplete()
completion_finder()
```