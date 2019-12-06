$(document).ready(function() {
    
    $('#newButton').click(function() {
        getFact();
    });

    // gets a random fact
    function getFact() {
        var settings = {
            "async": true,
            "crossDomain": false,
            "url": '/home/get-kris-fact?key=1234',
            "method": "GET"
        };
    
        $.ajax(settings).done(function (response) {
            const newFact = response['fact'];
            $('#factHeader').text(newFact);
        });
    }
});