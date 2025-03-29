// jshint esversion: 6

// Injects and updates the year of the footer copyright year
document.getElementById('copyright-date').innerHTML = (new Date().getFullYear());

// Set timeout for alert messages
setTimeout(function () {
    $('#message').fadeOut('slow');
}, 6000)