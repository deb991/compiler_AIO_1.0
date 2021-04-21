const { remote, ipcRenderer, app} = require('electron');
const TabGroup = require("electron-tabs");
//const mainProcess = require('main.js'); // plug in main process
const parser = new DOMParser();
const dragula = require("dragula");
const url = require('url');
const dialog = require('electron').dialog;
const path = require('path');
const fs = require('fs').remote;
const {ipcMain} = require('electron');
const {Menu} = remote;
const codeBdy = document.querySelector("editor.content")

// 2. Define the instance of the tab group (container)
let tabGroup = new TabGroup({
    ready: tabGroup => {
            dragula([tabGroup.tabContainer], {
                direction: "horizontal" 
            });
        },
    newTab: {
        title: 'Python Tab',
        // The file will need to be local, probably a local-ntp.html file
        // like in the Google Chrome Browser.

        src: "./Script_Editors/Python_ex.html",
        visible: true,
        //active: true,
        webviewAttributes: {
            nodeintegration: true
        }
    }
});

// 3. Add a tab from a website


let welcomeTab = tabGroup.addTab({
    title: "Welcome to JaRine",
    src: "./console_contents/welcome.html",
    visible: true,
    active: true,
    webviewAttributes: {
        nodeintegration: true
    }
});

//ipcRenderer.on('open-in-default', openInDefaultApplication)

// 4. Add a new tab that contains a local HTML file
let pythonTab = tabGroup.addTab({
    title: 'Demo Python Tab',
    src: "./Script_Editors/Python_ex.html",
    visible: true,
    //If the page needs to access Node.js modules, be sure to
    //enable the nodeintegration
    webviewAttributes: {
        nodeintegration: true
    }

});

ipcRenderer.on('addTab', (event, arg, file, content) => {
    tabGroup.addTab({
        title: mainProcess.file,
        src: "./Script_Editors/Python_ex.html",
        visible: true,
        webviewAttributes: {
            nodeintegration: true
        },
    })
});

const currentWindow = remote.getCurrentWindow();

const getDraggedFile = (event) => event.dataTransfer.items[0];
const getDroppedFile = (event) => event.dataTransfer.files[0];
const fileTypeIsSupported = (file) => {
 return ['text/plain', 'text/python'].includes(file.type);
};

const contextmenu = Menu.buildFromTemplate([
    //{label: 'Open', click(){mainProcess.getFileFromUser();}},
    //{label: 'New File', click(){mainProcess.getFileFromUser();}}
]);

//const updateUITitle = (isEdited) => {
//    let title = 'Jarine IDE';
//    if (filePath) { title: `${path.basename(filePath)} - //${title}`; }
//    if (isEdited) {title: `${title} (Edited)`; }

//    currentWindow.setTitle(title);
//    currentWindow.setDocumentEdited(isEdited);
//};

ipcRenderer.on('Open', (event, file, content) => {
    tabGroup.addTab({
        title: "opened File",
        src: "./Script_Editors/Python_ex.html",
        visible: true,
        webviewAttributes: {
            nodeintegration: true
        },
        //codeBdy.value = content
    })
  }).then(return());

document.addEventListener('dragstart', event => event.preventDefault());
document.addEventListener('dragover', event => event.preventDefault());
document.addEventListener('dragleave', event => event.preventDefault());
document.addEventListener('drop', event => event.preventDefault());
