/* Enable contenttools editor upon load.  Simple and prone to error approach.
 * Allows to disable editor with edit_off parameter.
 */

// Helper function to find get parameter in url.
// Required in order to detect edit_off.
function findGetParameter(parameterName) {
    var result = null,
        tmp = [];
    var items = location.search.substr(1).split("&");
    for (var index = 0; index < items.length; index++) {
        tmp = items[index].split("=");
        if (tmp[0] === parameterName) result = decodeURIComponent(tmp[1]);
    }
    return result;
}

// If there is no edit_off parameter initialise contenttools editor.  Upon
// saving the editor fold it's data into form and send to the backend as
// synchronous POST requiest.
if (!findGetParameter('edit_off')) {
  window.addEventListener('load', function() {
    var editor;
    // Ditch images. Hardcoded illusion that image sits at
    // first position in third row of default_tools.
    // So it will be broken at some point.
    ContentTools.DEFAULT_TOOLS[2].splice(0, 1)
    editor = ContentTools.EditorApp.get();
    editor.init('*[data-editable]', 'data-name');
    editor.addEventListener('saved', function (ev) {
      var regions;
      regions = ev.detail().regions;
      if (Object.keys(regions).length == 0) {
          return;
      }
      for (name in regions) {
          if (regions.hasOwnProperty(name)) {
              document.getElementById(name).value = regions[name];
          }
      }
      document.getElementById('update_form').submit();
    });
  });
}
