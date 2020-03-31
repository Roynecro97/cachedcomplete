# cachedcomplete

Cached wrapper for python argcomplete.

## Installation

Use the package manager pip to install cachedcomplete.

```bash
pip install cachedcomplete
activate-global-python-argcomplete
```

## Explanation

cachedcomplete wraps argcomplete, and allows caching of its parsers
in order to save up time.

cachedcomplete re-caches every time a change was made in itself,
or in the files specified by the user.

cachedcomplete caches the parsers using pickle, which implies the parser
must be able to be serialized and de-serialized using pickle.

Without any interference argparse's parsers cannot be serialized using pickle,
because the default type is defined within the parser's `__init__` function.
cachedcomplete replaces the default type with an identical type that can be pickled
(this is only done when cachedcomplete detects that the default type is still the default
identity function).

## Usage

### Normal Usage

The normal usage is the same as in argcomplete, only changing the import from argcomplete to cachedcomplete.

_**Note:** The usage of `PYTHON_ARGCOMPLETE_OK` stays the same as in argcomplete_

#### For Example

**Using argcomplete:**

```python
# PYTHON_ARGCOMPLETE_OK
import argcomplete

# ...

argcomplete.autocomplete()
```

**Using cachedcomplete:**

```python
# PYTHON_ARGCOMPLETE_OK
import cachedcomplete

# ...

cachedcomplete.autocomplete()
```

### Usage of custom subclasses of CompletionFinder

In order to use custom CompletionFinders with cachedcomplete,
a usage of the decorator cached_completion_finder is required.

#### For example

**Using argcomplete:**

```python
import argcomplete

class CustomCompletionFinder(argcomplete.CompletionFinder):
    # ...

completion_finder = CustomCompletionFinder()
# Instead of argcomplete.autocomplete()
completion_finder()
```

**Using cachedcomplete:**

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

**or:**

```python
import argcomplete
import cachedcomplete

class CustomCompletionFinder(argcomplete.CompletionFinder):
    # ...

completion_finder = cachedcomplete.cached_completion_finder(CustomCompletionFinder)()
# Instead of argcomplete.autocomplete()
completion_finder()
```

### Specifying what files to track

In order to specify which files to track changes in,
add a comment with the wanted files and the prefix CACHEDCOMPLETE_HASH:

```python
# CACHEDCOMPLETE_HASH: file1.py
```

It also allows multiple files split to multiple comments, or within one comment.

```python
# CACHEDCOMPLETE_HASH: file1.py file2.json
# CACHEDCOMPLETE_HASH: file3.py
# CACHEDCOMPLETE_HASH: "file with spaces.txt"
```

And also allows passing up a directory to track all the files within

```python
# CACHEDCOMPLETE_HASH: dir
```

Using environment variables and user directories is also allowed:

```python
# CACHEDCOMPLETE_HASH: $HOME/.cache/my-cache /tmp/${USERNAME}.ini
# CACHEDCOMPLETE_HASH: ~/.cache/my-cache ~gdm/greeter-dconf-defaults
```

Paths are relative to the calling script, not the current working directory.

cachedcomplete adds an environment variable name `pwd` to allow accessing the current
working directory in the comments. If this variable was already set, it is **not** overwritten.

```python
# CACHEDCOMPLETE_HASH: $pwd/local-file
```

### Using custom types, completers, actions, etc...

In order to cache a parser that uses your own custom types and functions,
they must be defined in a separate module than the main script (that defines the parser).

_**Note:** It is recommended to add these separate modules to the tracked files (As specified with `CACHEDCOMPLETE_HASH`)._

**Example:**

_Won't work:_

In `my_awesome_script.py`

```python
# PYTHON_ARGCOMPLETE_OK

import argparse
import cachedcomplete
import json

def json_file(arg):
    with argparse.FileType()(arg) as f:
        return json.load(f)

p = argparse.ArgumentParser()
p.add_argument('settings', type=json_file)
cachedcomplete.autocomplete(p)
```

_Will work:_

In `my_awesome_type.py`

```python
import json

def json_file(arg):
    with argparse.FileType()(arg) as f:
        return json.load(f)
```

In `my_awesome_script.py`

```python
# PYTHON_ARGCOMPLETE_OK
# CACHEDCOMPLETE_HASH: my_awesome_type.py

import argparse
import cachedcomplete

p = argparse.ArgumentParser()
p.add_argument('settings', type=json_file)
cachedcomplete.autocomplete(p)
```
