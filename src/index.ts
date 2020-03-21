import {
  JupyterFrontEnd, JupyterFrontEndPlugin
} from '@jupyterlab/application';

import {SnippetsBrowser} from './snippets';

const PLUGIN_ID = 'mkzilla:notebook-snippets';

/**
 * Initialization data for the jupyterlab-snippets extension.
 */
const extension: JupyterFrontEndPlugin<void> = {
  id: PLUGIN_ID,
  autoStart: true,
  activate: activate,
};

function activate(app: JupyterFrontEnd) {
  const snippetsBrowser = new SnippetsBrowser(app);
  app.shell.add(snippetsBrowser, 'left', { rank: 300 });
}

export default extension;
