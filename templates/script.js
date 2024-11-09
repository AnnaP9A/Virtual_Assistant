// script.js

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('userInputForm');
    const responseText = document.getElementById('responseText');

    form.addEventListener('submit', async function(event) {
        event.preventDefault();
        const formData = new FormData(form);
        const userInput = formData.get('user_input');

        const response = await fetch('/process_input', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: `user_input=${encodeURIComponent(userInput)}`
        });

        const responseData = await response.json();
        responseText.textContent = responseData.response;
    });
});
