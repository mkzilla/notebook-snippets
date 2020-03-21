import {PanelLayout, Widget} from '@lumino/widgets';
import {JupyterFrontEnd} from '@jupyterlab/application';
import {Clipboard} from '@jupyterlab/apputils';
import {CodeCellModel} from '@jupyterlab/cells';
import {ServerConnection} from "@jupyterlab/services";

const JUPYTER_CELL_MIME = 'application/vnd.jupyter.cells';


export class SnippetsBrowser extends Widget {

  constructor(app: JupyterFrontEnd) {
    super();
    this.title.caption = 'jupyterlab code snippets';
    this.id = 'jupyterlab-snippets-browser';

    this.layout = new PanelLayout();
    this.addClass("jp-SnippetsBrowser");

    this.sl = new SnippetsList(app);

    (this.layout as PanelLayout).addWidget(this.sl);
    this.sl.refresh('');
  }

  readonly sl: SnippetsList;
}

export class SnippetsList extends Widget {
  private _ul: HTMLUListElement;
  private _header: HTMLHeadElement;
  snippets: SnippetsCommand[] = [];
  app: JupyterFrontEnd;

  constructor(app: JupyterFrontEnd) {
    super();
    this.app = app;
    const layout = (this.layout = new PanelLayout());
    const wrapper = new Widget();
    wrapper.addClass("jp-SnippetsList");
    this._ul = document.createElement('ul');
    this._header = document.createElement('header');
    this._header.innerText = 'Code Snippets';
    wrapper.node.appendChild(this._header);
    wrapper.node.appendChild(this._ul);
    layout.addWidget(wrapper);
  }

  refresh(name: string) {
    let settings = ServerConnection.makeSettings();
    ServerConnection.makeRequest(settings.baseUrl + 'snippets',  {method: 'GET'}, settings).then((response) => {
      if (response.status != 200) {
        return
      }
      response.json().then((data) => {
        this.snippets = [];
        data.map((m: any) => {
          let md = new SnippetsCommand(this.app,m);
          this.snippets.push(md);
          this._ul.appendChild(md.html());
        });
      }).catch((e) => {
        console.log(e);
      });
    });
  }
}

export class Snippets {
  name: string;
  snippets: string[];
}

export class SnippetsCommand extends Widget {
  snippets: Snippets;
  private _div: HTMLDivElement;
  constructor(app: JupyterFrontEnd,snippets: Snippets) {
    super();
    this.snippets = snippets;
    this._div = document.createElement('div');
    let self = this;
    this._div.onclick = function () {
      const clipboard = Clipboard.getInstance();

      let cell = new CodeCellModel({cell:
          {
            cell_type: "code",
            metadata: { trusted: false },
            source: [
              self.snippets.snippets.join('\n')
            ]
          }
      });
      clipboard.setData(JUPYTER_CELL_MIME, [cell.toJSON()]);
      app.commands.execute('notebook:paste-cell-below',{});
      clipboard.clear();
    }
  }

  html() {
    this._div.innerHTML = `<li><a>${this.snippets.name}</a><i class="fa fa-arrow-circle-right" aria-hidden="true"></i></li>`;
    return this._div;
  }
}