// jshint esversion: 6

// Injects and updates the year of the footer copyright year
document.getElementById('copyright-date').innerHTML = (new Date().getFullYear());

// Set timeout for alert messages
setTimeout(function () {
    $('#message').fadeOut('slow')
}, 6000)

// Event listener for Order form billing details submission
document.addEventListener('DOMContentLoaded', function () {
    var placeOrderBtn = document.getElementById('placeOrderBtn');
    var hiddenSubmitBtn = document.getElementById('hiddenSubmitBtn');

    if (placeOrderBtn && hiddenSubmitBtn) {
        placeOrderBtn.addEventListener('click', function () {
            // Trigger the click event of the hidden submit button
            hiddenSubmitBtn.click();
        });
    }
});