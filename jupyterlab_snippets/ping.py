import platform
import os
import socket
from notebook.base.handlers import IPythonHandler
from ._version import __version__


class ping(IPythonHandler):
    def get(self):
        data = dict(
            os = platform.system(),
            arch = platform.architecture(),
            platform = platform.platform(),
            platform_version = platform.version(),
            processor = platform.processor(),
            node = socket.getfqdn(),
            python = platform.python_version(),
            labserver_version = __version__,
            user = os.environ.get('USER'),
            query= self.request.query,
        )
        self.finish(data)