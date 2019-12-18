$(document).ready(function() {

    // Click event for Strategy pattern list item
    $('#list-sp').click(function () {
        const modal = $('#list-sp-modal');
        modal.removeClass('hide-modal');
    });

    // Click event for DRY list item
    $('#list-dry').click(function () {
        const modal = $('#list-dry-modal');
        modal.removeClass('hide-modal');
    });

    // Click event for Command pattern list item
    $('#list-cp').click(function () {
        const modal = $('#list-cp-modal');
        modal.removeClass('hide-modal');
    });

    // Click event for TODO list item
    $('#list-todo').click(function () {
        const modal = $('#list-todo-modal');
        modal.removeClass('hide-modal');
    });
    // -------------------------------------

    // Modal closing event
    $('.p-modal').click(function(e) {
        if(e.target !== this) {
            return;
        }
        $(this).addClass('hide-modal');
    });
});