import imp
import os
import sys


def setup_django_env(path):
    from django.core.management import setup_environ
    try:
        module_info = imp.find_module('settings', [path])
        settings = imp.load_module('settings', *module_info)

        setup_environ(settings)
    except ImportError:
        msg = "Error: Can't find 'settings.py' in configured PYTHON_PATH", path
        print >> sys.stderr, msg
        sys.exit(1)


# shovel/ directory should be placed at the same level of settings.py
setup_django_env(os.getcwd())
