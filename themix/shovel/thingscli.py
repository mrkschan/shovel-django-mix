# Task file name should NOT be the same as the django app name

try:  # Load the django environment
    import imp
    import os
    import sys

    me = os.path.abspath(os.path.dirname(__file__))
    module_info = imp.find_module('context', [me])
    imp.load_module('context', *module_info)
except:
    print >> sys.stderr, 'Cannot setup Python environment from context.py'


from shovel import task
from things.models import Thing


@task
def list():
    '''List all things'''
    for i in Thing.objects.all():
        print i.name
