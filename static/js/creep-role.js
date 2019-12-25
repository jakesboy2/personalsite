$(document).ready(function (){
    
    const allBios = {
        "miner": $('#miner-bio'),
        "harvester": $('#harvester-bio'),
        "worker": $('#worker-bio'),
        "claimer": $('#claimer-bio'),
        "mineral": $('#mineral-bio'),
        "power": $('#power-bio'),
        "rcolonizer": $('#r-colonizer-bio'),
        "rminer": $('#r-miner-bio'),
        "rharvester": $('#r-harvester-bio'),
        "rreserver": $('#r-reserver-bio'),
        "manager": $('#manager-bio'),
        "ddefender": $('#d-defender-bio'),
        "rdefender": $('#r-defender-bio'),
        "zealot": $('#zealot-bio'),
        "stalker": $('#stalker-bio'),
        "medic": $('#medic-bio'),
        "dmedic": $('#d-medic-bio'),
        "dtank": $('#d-tank-bio'),
        "scout": $('#scout-bio'),
        "lorry": $('#lorry-bio'),
    }

    // Miner Click Event
    $('#miner-row').click(function() {
        const currentBio = allBios["miner"];
        hideAll();
        showOne(currentBio);
    });

    // Harvester Click Event
    $('#harvester-row').click(function() {
        const currentBio = allBios["harvester"];
        hideAll();
        showOne(currentBio);
    });

    // Miner Click Event
    $('#lorry-row').click(function() {
        const currentBio = allBios["lorry"];
        hideAll();
        showOne(currentBio);
    });

    // Harvester Click Event
    $('#claimer-row').click(function() {
        const currentBio = allBios["claimer"];
        hideAll();
        showOne(currentBio);
    });

    // Miner Click Event
    $('#mineral-row').click(function() {
        const currentBio = allBios["mineral"];
        hideAll();
        showOne(currentBio);
    });

    // Harvester Click Event
    $('#power-row').click(function() {
        const currentBio = allBios["power"];
        hideAll();
        showOne(currentBio);
    });

    // Miner Click Event
    $('#r-miner-row').click(function() {
        const currentBio = allBios["rminer"];
        hideAll();
        showOne(currentBio);
    });

    // Harvester Click Event
    $('#r-harvester-row').click(function() {
        const currentBio = allBios["rharvester"];
        hideAll();
        showOne(currentBio);
    });

    // Miner Click Event
    $('#r-reserver-row').click(function() {
        const currentBio = allBios["rreserver"];
        hideAll();
        showOne(currentBio);
    });

    // Harvester Click Event
    $('#r-colonizer-row').click(function() {
        const currentBio = allBios["rcolonizer"];
        hideAll();
        showOne(currentBio);
    });

    // Miner Click Event
    $('#worker-row').click(function() {
        const currentBio = allBios["worker"];
        hideAll();
        showOne(currentBio);
    });

    // Harvester Click Event
    $('#manager-row').click(function() {
        const currentBio = allBios["manager"];
        hideAll();
        showOne(currentBio);
    });

    // Miner Click Event
    $('#d-defender-row').click(function() {
        const currentBio = allBios["ddefender"];
        hideAll();
        showOne(currentBio);
    });

    // Harvester Click Event
    $('#r-defender-row').click(function() {
        const currentBio = allBios["rdefender"];
        hideAll();
        showOne(currentBio);
    });

    // Miner Click Event
    $('#zealot-row').click(function() {
        const currentBio = allBios["zealot"];
        hideAll();
        showOne(currentBio);
    });

    // Harvester Click Event
    $('#stalker-row').click(function() {
        const currentBio = allBios["stalker"];
        hideAll();
        showOne(currentBio);
    });

    // Miner Click Event
    $('#medic-row').click(function() {
        const currentBio = allBios["medic"];
        hideAll();
        showOne(currentBio);
    });

    // Harvester Click Event
    $('#drainer-tank-row').click(function() {
        const currentBio = allBios["dtank"];
        hideAll();
        showOne(currentBio);
    });

    // Miner Click Event
    $('#drainer-medic-row').click(function() {
        const currentBio = allBios["dmedic"];
        hideAll();
        showOne(currentBio);
    });

    // Harvester Click Event
    $('#scout-row').click(function() {
        const currentBio = allBios["scout"];
        hideAll();
        showOne(currentBio);
    });

    // Add the class to hide the div to all the bios
    function hideAll() {
        for(let bio in allBios) {
            if(!allBios[bio].hasClass('hidden-heading')) {
                allBios[bio].addClass('hidden-heading');
            }
        }
    }

    // Remove the hidden class from the specific div
    function showOne(bio) {
        const wrapper = $('#creep-bio-div');
        if(!wrapper.hasClass('new-left-padding')) {
            wrapper.addClass('new-left-padding');
        }
        bio.removeClass('hidden-heading');
    }
});