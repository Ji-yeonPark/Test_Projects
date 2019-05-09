(function () {
    'use strict';
    var remote = require('electron').remote,
        app = remote.app,
        ipcRenderer = require('electron').ipcRenderer;

    var path,
        list,
        image = $(".image");

    // remove list items
    var removelist = () => {
        while (list.hasChildNodes()) {
            list.removeChild(list.firstChild);
        }
    }

    // remove preview image
    var removeimage = () => {
        while (image.hasChildNodes()) {
            image.removeChild(image.firstChild)
        }
    }

    // get extension
    var ext = (name) => {
        return name.split(".").pop()
    }

    // show preview image
    var show = (el) => {

        if ($('.list-group-item.active')) 
            $('.list-group-item.active').classList.remove("active");
        el.classList.add("active");

        /* Create Element
          <img src="" class="img-fluid rounded" alt="">
        */
        let img = document.createElement("img");
        img.setAttribute("src", el.dataset.path);
        img.setAttribute("class", "img-fluid rounded");
        img.setAttribute("alt", el.innerHTML);

        removeimage();
        image.append(img);

    }

    // main
    var finder = {
        // set init path. 
        set: function (element) {
            $('.path').value = app.getPath("pictures");
            list = $(element);
        },
        get: function () {
            path = $('.path').value;

            // send data to server and receive
            var obj = ipcRenderer.sendSync("find", {
                'path': path
            });

            var files = obj.files;
            if (!obj.result) alert(obj.message);

            removelist();
            removeimage();

            // append items at list
            obj.files.forEach(file => {
                file = file.replace(/\\/g, "/");
                let splitpath = file.split("/"),
                    filename = splitpath[splitpath.length - 1];

                if (ext(filename) === "png") {
                    /* Create Element
                      <button type="button" class="list-group-item list-group-item-action"></button>
                    */
                    let item = document.createElement('button');
                    item.className = "list-group-item list-group-item-action";
                    item.onclick = function () {
                        show(this)
                    };
                    item.title = file;
                    item.dataset.path = file + "?" + new Date().getTime();
                    item.innerHTML = filename;

                    list.append(item);
                }
            });

        }
    }

    module.exports = finder;

})();