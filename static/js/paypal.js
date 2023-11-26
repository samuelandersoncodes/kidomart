// // jshint esversion: 6

// Paypal integration
// This function loads the PayPal SDK dynamically
function loadPayPalScript(clientID, callback) {
    var script = document.createElement('script');
    script.src = `https://www.paypal.com/sdk/js?client-id=${clientID}&currency=USD`;
    script.async = true;
    script.defer = true;
    script.onload = function () {
        callback();
    };
    document.head.appendChild(script);
}

var payment_method = 'PayPal'

// Function to set up the PayPal button
function setupPayPalButton() {
    paypal.Buttons({
        env: 'sandbox',
        createOrder: function (data, actions) {
            // Set up the transaction with the global variable as the amount
            return actions.order.create({
                purchase_units: [{
                    amount: {
                        value: totalAmount,
                    }
                }]
            });
        },
        onApprove: function (data, actions) {
            // Capture the funds from the transaction
            return actions.order.capture().then(function (details) {
                // Display a success message to the user
                sendData()
                function sendData() {
                    fetch(paymentUrl, {
                        method : "POST",
                        headers: {
                            "Content-type": "application/json",
                            "X-CSRFToken": csrftoken,
                        },
                        body: JSON.stringify({
                            orderID: orderID,
                            transID: details.id,
                            payment_method: payment_method,
                            status: details.status
                        }),
                    })               
                }
            }).catch(function (error) {
                // Log the detailed error information
                console.error('Error capturing funds:', error);
                console.error('Error details:', error.details.originalError.response);
                // Handle the error or notify the user appropriately
            });
        },
    }).render('#paypal-button-container');
}