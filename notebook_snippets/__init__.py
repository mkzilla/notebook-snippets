from notebook.utils import url_path_join

from ._version import __version__
from .ping import ping
from .snippets import snippets


def _jupyter_server_extension_paths():
    return [{
        'module': 'jupyterlab_snippets'
    }]


def load_jupyter_server_extension(nb_server_app):
    web_app = nb_server_app.web_app
    base = web_app.settings['base_url']
    host_pattern = '.*$'

    web_app.add_handlers(host_pattern, [
        (url_path_join(base, r"/ping"), ping),
        (url_path_join(base, r"/snippets"), snippets),
    ])