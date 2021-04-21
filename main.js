/**
 * @Author: Deva Biswas
 * @Date:   2020-06-07T17:48:02+05:30
 * @Email:  net.aphos@yandex.com
 * @Project: JrineCloudPlatform
 * @Filename: main.js
 * @Last modified by:   Deva Biswas
 * @Last modified time: 2021-03-13T03:33:18+05:30
 * @License: MIT License
 * @Copyright: @deb991
 */



const { app, BrowserWindow, Menu, MenuItem, ipcRenderer, dialog} = require('electron');
const contextMenu = require('electron-context-menu');
const path = require('path')
const url = require('url')
const ipc = require('electron').ipcMain;
const fs = require('fs');
const {ipcMain} = require('electron')
const applicationMenu = require('./app_menu');

let win = null;


// Create the browser window.
function createWindow () {
    win = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            nodeIntegration: true,
            webviewTag: true,
            enableRemoteModule: true
        }
    });

    // and load the index.html of the app.
    win.loadFile('./index.html')
    //win.loadURL('file://' + __dirname + './index.html');
    win.on('ready-to-show', ()  => {
        win.show();
        getFileFromUser.show();
        //win.focus();
    });
  // Open the DevTools.
  //win.webContents.openDevTools()
}


//const menu = Menu.buildFromTemplate(template) <<<<<<<<<<<<<<<<<<<<<<<<<<
//Menu.setApplicationMenu(menu)   <<<<<<<<<<<<<<<<<<<<<<<<
app.on('ready', () => {
    Menu.setApplicationMenu(applicationMenu);
    createWindow();
});



const getFileFromUser = exports.getFileFromUser = (win) => {
    const files = dialog.showOpenDialog(win, {
        properties: ['OpenFile'],
        filters: [
            {name: 'Files', extensions: ['txt']},
            {name: 'Python', extensions: ['py', 'python', 'applications']}
        ]
    });

    if (!files) {openFile(files[0])
    }
    console.log(files);
};



const OpenFile = exports.openFile = (win, file) => {
    const content = fs.readFileSync(file).toString();
    app.addRecentDocument(file);
    app.tabGroup.setRepresentedFilename(file);
    win.tabGroup.webContents.send('file-opened', file, content);
    console.log(content)
};


const saveFile = exports.saveFile = (targetWindow, content) => {
    if (!file) {
        file = dialog.showSaveDialog(targetWindow, {
            title: 'Save file',
            defaultPath: app.getPath('documents'),
            filters: [
                { name: 'Python Script', extensions: ['py', 'pyc'] }
            ]
        });
        if (!file) return;
        fs.writeFileSync(file, content);
    }
};
