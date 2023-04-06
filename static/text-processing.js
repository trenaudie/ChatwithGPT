document.getElementById('text-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const userInput = document.getElementById('user-input').value;
    const responseDiv = document.getElementById('text-response');

    try {
        const response = await fetch('/process_text', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text: userInput }),
        });

        if (response.ok) {
            const data = await response.json();
            responseDiv.innerText = data.result;
        } else {
            responseDiv.innerText = 'Error processing the text.';
        }
    } catch (error) {
        console.error('Error:', error);
        responseDiv.innerText = 'Error processing the text.';
    }
});
