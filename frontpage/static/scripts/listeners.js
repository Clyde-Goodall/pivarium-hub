//for pulling data into charts and updating via websocket
//still old code in here for reusability, but will be eventually removed

$(document).ready(function() {
    //calls new socket from class in socket.js
    console.log(current_station);
    var interval = true;
    var socke = new createSocket("/ws/frontend/");
    socke.socket.onopen = function() {
        console.log("Established. Requesting data");
        data = '{ "first": "true", "chart": "true", "current_station": "' + current_station + '", "interval" : "' + interval + '"}';
        socke.pushToServer(data);
    }

    socke.socket.onmessage = function(e) {
        alert(e.data);
        console.log("Message received: ");
        data = JSON.parse('' + e.data + '');
        console.log(data.data);
    }



    //adds first pull to chart
    function populateChart(symbol) {

        // todo

    }

    //updates chart
    function updateChart(oldS, newS) {
        //action: update,delete, or submit
        json = '{ "action": "update", "old":"' + oldS + '" , "new" : "' + newS + '"}';

        socke.pushToServer(json);

    }

});