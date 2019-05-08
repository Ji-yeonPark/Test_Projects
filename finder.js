(function () {
    'use strict';
    var remote = require('electron').remote,
        app = remote.app,
        ipcRenderer = require('electron').ipcRenderer;

    var path;

    // main
    var finder = {
        // set init path. 
        set: function () {
            $('.path').value = app.getPath("pictures");
        },
        get: function () {
            path = $('.path').value;

            ipcRenderer.send("find", {
                'path': path
            })
        }
    }



    if (typeof define == 'function' && define.amd) {
        define(function () {
            return finder;
        });
    } else if (typeof module !== 'undefined') {
        module.exports = finder;
    } else {
        window.Finder = finder;
    }

})();