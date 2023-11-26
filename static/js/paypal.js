// jshint esversion: 6

// Paypal integration
// This function loads the PayPal SDK dynamically
function loadPayPalScript(clientID, callback) {
    var script = document.createElement('script');
    script.src = `https://www.paypal.com/sdk/js?client-id=${clientID}&currency=USD`;
    script.async = true;
    script.defer = true;
    script.onload = callback;
    document.head.appendChild(script);
}

// Function to set up the PayPal button
function setupPayPalButton() {
    paypal.Buttons({
        createOrder: function (data, actions) {
            // Set up the transaction
            return actions.order.create({
                purchase_units: [{
                    amount: {
                        value: '11.00'
                    }
                }]
            });
        },
        onApprove: function (data, actions) {
            // Capture the funds from the transaction
            return actions.order.capture().then(function (details) {
                // Display a success message to the user
                alert('Transaction completed by ' + details.payer.name.given_name + '!');
            });
        }
    }).render('#paypal-button-container');
}