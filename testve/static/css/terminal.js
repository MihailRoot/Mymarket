import { Terminal }  from './node_modules/xterm/lib/xterm.js';
import  { AttachAddon } from './node_modules/xterm-addon-attach/lib/xterm-addon-attach.js';
const terminal = new Terminal();
const attachAddon = new AttachAddon(webSocket);
terminal.loadAddon(attachAddon);
