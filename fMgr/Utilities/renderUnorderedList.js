static renderUnorderedListHtml(files) {
    return (
        <ul>
            {files.map((file, i) => {
                return (
                    <li key={i}>
                        <span>{file.name}</span>
                        {file.items.length > 0 &&
                            FileTree.renderUnorderedListHtml(file.items)
                        }
                    </li>
                )
            })}
        </ul>
    )
}