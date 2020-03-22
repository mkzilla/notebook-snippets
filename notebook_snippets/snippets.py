from notebook.base.handlers import IPythonHandler
from .code import numba, python, python_regex
import json


arr = []

arr = arr + python.code + python_regex.code + numba.code


class snippets(IPythonHandler):
    def get(self):

        self.finish(json.dumps(arr))