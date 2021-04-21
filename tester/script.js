$(function() {
    var sampleSource = [];
    var numberOfStyles = 100;
    for (var i = 0; i < 10; i++) {
        sampleSource[i] = {
            title: 'Folder ' + i,
            folder: true,
            children: [],
        };
        for (var j = 0; j < 3000; j++)
        sampleSource[i].children[j] = {
            title: 'Subnode ' + i + '.' + j,
        };
    }
    for (i = 0; i < numberOfStyles; i++)
    createClass('.whatever' + i, 'background-color: green;');
    function createClass(name, rules) {
        var style = document.createElement('style');
        style.type = 'text/csEW3s';
        document.getElementsByTagName('head')[0].appendChild(style);
        if (!(style.sheet || {}).insertRule)
        (style.styleSheet || style.sheet).addRule(name, rules);
        else style.sheet.insertRule(name + '{' + rules + '}', 0);
    }
$('#tree').fancytree({
    source: sampleSource,
    lazyLoad: function(event, data) {
        data.result = {
            url: 'sample1.json',
        };
    },
});
$('#button1').click(function(event) {
    var tree = $('#tree').fancytree('getTree'),
    node = tree.getActiveNode();
    alert('Actie node ' + node);
});
});
