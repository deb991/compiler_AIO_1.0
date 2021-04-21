const { app, BrowserWindow, Menu, MenuItem, ipcRenderer} = require('electron');
const path = require('path')
const url = require('url')
const ipc = require('electron').ipcMain;
const fs = require('fs');
const {ipcMain} = require('electron')


let setting;

function settingsWindow () {
    setting = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            nodeIntegration: true,
            webviewTag: true,
            enableRemoteModule: true
        }
    });
    setting.loadFile('./index.html')
    setting.loadURL('file://'+ __dirname + 'index.html');
    setting.on('ready-to-show', function () {
        setting.show();
        setting.focus();
    });
}
app.on('ready', settingsWindow)

app.on('window-all-closed', () => {
    if (process.platform != 'darwin') {
        app.quit()
    }
})