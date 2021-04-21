const jstree = require("jstree")
$(document).ready(function() {
  $('#data').jstree({

    "plugins": ["checkbox"]
  });

$("#data").on("changed.jstree", function(e, data){
  if (data.selected.length) {

    $(data.selected).each(function(idx){
      var node = data.instane.get_node(data.selected(idx));
      console.log("This selected Node is: " + node.text);
    });
  }
});
});
