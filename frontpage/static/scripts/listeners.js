//for pulling data into charts and updating via websocket
//still old code in here for reusability, but will be eventually removed



$(document).ready(function() {
    //calls new socket from class in socket.js
    console.log(current_station);
    var interval = true;
    var socket = new WebSocket('ws://' + window.location.host + '/ws/frontend/');

    socket.onmessage = function(e) {
        console.log("Message received: ");
        ne = JSON.parse(e.data);
        console.log(ne.data);
        console.dir(ne.data[2]);
    }


    socket.onopen = function() {
        console.log("Established. Requesting data");
        data = '{ "first": "true", "chart": "true", "current_station": "' + current_station + '", "interval" : "' + interval + '"}';
        socket.send(data);
    }


    //adds first pull to chart
    function populateChart(symbol) {

        // todo

    }

    //updates chart
    function updateChart(oldS, newS) {
        //action: update,delete, or submit
        json = '{ "action": "update", "old":"' + oldS + '" , "new" : "' + newS + '"}';

        socket.send(json);

    }

});