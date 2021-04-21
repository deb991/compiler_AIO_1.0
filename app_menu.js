/**
 * @Author: Deva Biswas
 * @Date:   2020-07-16T22:26:59+05:30
 * @Email:  net.aphos@yandex.com
 * @Project: JrineCloudPlatform
 * @Filename: app_menu.js
 * @Last modified by:   Deva Biswas
 * @Last modified time: 2021-03-13T03:37:14+05:30
 * @License: MIT License
 * @Copyright: @deb991
 **/



const {app, browserWindow, dialog, Menu, shell} = require('electron');
const mainProcess = require('./main').remote;
//const renderer = require('./renderer').remote;


const template = [
    {
        label: 'WorkSpace',  //File menu has not been developed. Need to develop/ define.
        submenu: [
            {
                label:'Open',
                accelerator: 'CmdOrCtrl+O',
                click(menuItem, browserWindow, event) {
                  browserWindow.webContents.send('addTab', {
                     title: 'Test tab',
                     visible: true
                  })
                    mainProcess.getFileFromUser().remote;
                    codeBdy.value = content;
                    focusWindow.webContents.send('open-in-default');
                }

                //click: function(menuItem, browserWindow, event) //{
                  //browserWindow.webContents.send('addTab', {
                //     title: mainProcess.file,
                  //   visible: true
                  //})
                  //mainProcess.getFileFromUser();
               //}
            },
            {
                label:'New File',
                //accelerator: 'CmdOrCtrl+O',
                click: function(menuItem, browserWindow, event) {
                   browserWindow.webContents.send('addTab', {
                      title: 'Test tab',
                      visible: true
                   })

                }
            },
            {
                type:'separator'
            },
            {
                label:'New Project',
                //accelerator: 'CmdOrCtrl+O',
                click() { CreateNewProject(); }
            },
            {
                label:'Open Projects',
                //accelerator: 'CmdOrCtrl+O',
                click() { OpenProjectList(); }
            },
            {
                label:'Close Project',
                //accelerator: 'CmdOrCtrl+O',
                click() { CloseCurrentProject(); }
            },
            {
                type:'separator'
            }
        ]
    },
    {
      label: 'Edit',
      submenu: [
         {
            role: 'undo'
         },
         {
            role: 'redo'
         },
         {
            type: 'separator'
         },
         {
            role: 'cut'
         },
         {
            role: 'copy'
         },
         {
            role: 'paste'
         },
         {
            label: 'Configuration',
            //click: settingsWindow
         }
      ]
   },
    {
      label: 'View',
      submenu: [
         {
            role: 'reload'
         },
         {
            role: 'toggledevtools'
         },
         {
            type: 'separator'
         },
         {
            role: 'resetzoom'
         },
         {
            role: 'zoomin'
         },
         {
            role: 'zoomout'
         },
         {
            type: 'separator'
         },
         {
            role: 'togglefullscreen'
         }
      ]
   },
    {
        label: 'Navigation',
        submenu: [
            {
                label: 'class'
            },
            {
                label: 'file'
            },
            {
                label: 'symbol'
            },
            {
                label: 'custom folding'
            },
            {
                label: 'line/column'
            },
            {
                type:'separator'
            },
            {
                label: 'Super Method'
            },
            {
                label: 'file structure'
            }
        ]
    },
    {
      role: 'window',
      submenu: [
         {
            role: 'minimize'
         },
         {
            role: 'close'
         }
      ]
   },
    {
       role: 'help',
      submenu: [
         {
            label: 'Learn More'
         }
      ]
   }
];

if (process.platform === 'darwin') {
   const name = app.getName();
   template.unshift({ label: name });
  }

module.exports = Menu.buildFromTemplate(template);
