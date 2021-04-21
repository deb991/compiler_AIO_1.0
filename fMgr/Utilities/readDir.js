static readDir(path) {
    var fileArray = [];

    electronFs.readdirSync(path).forEach(file => {
        var fileInfo = new FileTree(`${path}\\${file}`, file);

        var stat = electronFs.statSync(fileInfo.path);

        if (stat.isDirectory()){
            fileInfo.items = FileTree.readDir(fileInfo.path);
        }

        fileArray.push(fileInfo);
    })

    return fileArray;
}