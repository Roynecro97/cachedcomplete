import argparse
import json

import os
os.write(0, b'\Running imported_module.py\n')

def json_file(arg):
    with argparse.FileType()(arg) as f:
        return json.load(f)

def completer(**kwargs):
    import completer_specific_module
    return [attr for attr in dir(completer_specific_module) if not attr.startswith('_')]
