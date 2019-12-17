$(document).ready(function (){
    
    $('#about-btn').click(function () {
        switchAboutView();
    });

    // Switch the about section view from philosophy or about screeps
    function switchAboutView() {
        const aboutScreeps = $('#about-screeps');
        const aboutCode = $('#about-code');
        const codeContent = $('#about-code-content');
        const screepsContent = $('#about-screeps-content');
        const aboutBtn = $('#about-btn');

        // Toggle the divs being shown to show the correct combo based on which div currently has the hidden class
        // Toggle text on the button
        if(aboutCode.hasClass('hidden-heading')) { 
            // The View Our Philosophy button was clicked
            aboutCode.removeClass('hidden-heading');
            aboutScreeps.addClass('hidden-heading');

            codeContent.removeClass('hidden-heading');
            screepsContent.addClass('hidden-heading');

            aboutBtn.text("Learn More About Screeps");
        }
        else {
            // The learn more about screeps button was clicked
            aboutScreeps.removeClass('hidden-heading');
            aboutCode.addClass('hidden-heading');

            screepsContent.removeClass('hidden-heading');
            codeContent.addClass('hidden-heading');

            aboutBtn.text("View Our Philosophy");
        }
    }
});