// jshint esversion: 6

// Injects and updates the year of the footer copyright year
document.getElementById('copyright-date').innerHTML = (new Date().getFullYear());

// Set timeout for alert messages
setTimeout(function () {
    $('#message').fadeOut('slow')
}, 6000)

//Event listener for Order form billing details submission
document.addEventListener('DOMContentLoaded', function () {
    var placeOrderBtn = document.getElementById('placeOrderBtn');
    var hiddenSubmitBtn = document.getElementById('hiddenPlaceOrderBtn');
    var form = document.getElementById('orderForm');

    if (placeOrderBtn && hiddenSubmitBtn && form) {
        placeOrderBtn.addEventListener('click', function () {
            // Triggers the form submission
            form.submit();
        });

        // Listens for the form submission event
        form.addEventListener('submit', function (event) {
            event.preventDefault();

            var formData = new FormData(form);

            fetch(form.action, {
                method: 'POST',
                body: formData
            })
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Sorry! Something went wrong');
                    }
                    return response.text();
                })
                .then(() => {
                    // Redirects to payments.html
                    window.location.href = '/orders/payments/';
                })
                .catch(error => {
                    console.error('Error:', error);
                    // Handles errors
                });
        });
    }
});