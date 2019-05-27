const {
    app,
    BrowserWindow,
    ipcMain
} = require('electron')
const path = require('path')
const url = require('url')


let win
let child

function createWindows() {

    win = new BrowserWindow({
        width: 800,
        height: 600,
        show: false,
        webPreferences: {
            nodeIntegration: true
        }
    })

    win.loadURL(url.format({
        pathname: path.join(__dirname, 'index.html'),
        protocol: 'file',
        slashes: true
    }))

    child = new BrowserWindow({
        parent: win,
        width: 400,
        height: 800,
        webPreferences: {
            nodeIntegration: true
        }
    })
    child.loadURL(url.format({
        pathname: path.join(__dirname, 'login.html'),
        protocol: 'file',
        slashes: true
    }))

    child.openDevTools();

     win.on('closed', function () {
        win = null;
    })


}

ipcMain.on('entry-accepted', (event, arg) => {
    if (arg == 'ping') {
        win.maximize(); // 윈도우 풀스크린으로 활성화
        win.show()
        child.hide()
    }
})

app.on('ready', createWindows);
app.on('activate', function () { // 애플리케이션이 활성화될 때
    if (win === null) {
        createWindow()
    }
});
