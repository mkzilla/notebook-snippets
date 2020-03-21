from notebook.base.handlers import IPythonHandler
import json

code = [
    {
        'name':'Setup',
        'snippets': [
            'from __future__ import print_function, division',
            'import sys',
            'if sys.version_info[0] >= 3:',
            '    xrange = range  # Must always iterate with xrange in njit functions',
            'import numba',
        ]
    }

]


class snippets(IPythonHandler):
    def get(self):
        self.finish(json.dumps(code))