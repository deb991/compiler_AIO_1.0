import React, { Component } from 'react';
import './App.css';
import FileTree from './Utilities/FileTree';
var remote = window.require('electron').remote;
var { dialog } = remote;

class App extends Component { 
  constructor(props){
    super(props);

    this.state = {
      fileTree: null
    }
  }
  
  render() {
    var filetree = this.state.fileTree
      ? this.state.fileTree.renderUnorderedList()
      : null;

    return (
      <div>
        <button onClick={this.handleOpenFolder}>Open Folder</button>
        <div id="filetree">
          {filetree}
        </div>
      </div>
    );
  }

  handleOpenFolder = () => {
    var directory = dialog.showOpenDialog({ properties: ['openDirectory']});

    if (directory && directory[0]){
      var fileTree = new FileTree(directory[0]);

      fileTree.build();

      this.setState({fileTree});
    }

  }
}

export default App;
