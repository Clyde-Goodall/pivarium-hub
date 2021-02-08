//for pulling data into charts and updating via websocket
//still old code in here for reusability, but will be eventually removed

$(document).ready(function() {
    //calls new socket from class in socket.js
    var socke = new createSocket("/ws/frontend/");

    socke.socket.onmessage = function(e) {
        console.log(e.data);
        //django can really only send text data, so it gets re-converted to json
        data = {
            "charts": True
        };
        console.log(data);
        socke.pushToServer("connection requested")
            //data.value = symbol
            //data.action = submit, delete, or update


    }

    //submits symbol to server using return key

    //removes symbol <td>. Is problematic when dealing with 
    //dynamically .append() elements though, so not sure how to geta round that yet
    function removeSymbolElement(id) {
        $('.tr-' + id).remove();
    }

    //deletes symbol
    function deleteSymbol(symbol) {

        json = '{ "action": "delete", "value":"' + symbol + '" }';

        socke.pushToServer(json);

    }

    //updates previously added ticker
    function updateSymbol(oldS, newS) {
        //action: update,delete, or submit
        json = '{ "action": "update", "old":"' + oldS + '" , "new" : "' + newS + '"}';

        socke.pushToServer(json);

    }


    //send alert to client that the ticker symbol is invalid
    function returnError(error) {
        //todo: return why a user can't submit something based on the result from the server
    }


    $('.watchlist-table').on('click', '.mdl-button--icon', function() {
        console.log('edit clicked');
        getID = $(this).attr('id');
        $('input#' + getID).attr('disabled', false).select();
    });

    $('table').on('keypress', 'input.filled', function(e) {
        id = e.target.id;
        console.log(id);

        //If they hit return on a previously added symbol, it'll tell server to delete if empty, 
        //otherwise input with current value
        if (e.which == 13) {
            if ($(this).val().length == 0) {
                deleteSymbol(id);
            } else if ($(this).val().length > 0 && $(this).val().length < 8) {
                updateSymbol(id, $(this).val());
            }
        }
    });

    //re-disabled inputs when user leaves the input
    $(document).on('focusout', 'input.filled', function() {
        id = $(this).attr('id');
        if ($('input.filled').val().length == 0) {
            console.log("removing");
            $('input.filled').closest('tr-' + id).remove();
        } else {
            $('input.filled').attr('disabled', true);
        }


    });


});