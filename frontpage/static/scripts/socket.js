class createSocket {


    constructor(loc) {
        this.socket = new WebSocket('ws://' + window.location.host + loc);
        console.log(window.location.host)
        this.socket.onopen = function open() {
            console.log('WebSockets connection created.');
        };

        if (this.socket.readyState == WebSocket.OPEN) {
            this.socket.onopen();
        }

        this.socket.onmessage = function(e) {
            print(e.data);
            if (e.data == "symbol added") {

            }
        }
    }

    pushToServer(what) {
        this.socket.send(what);
    }


}