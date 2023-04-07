document.getElementById('text-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const userInput = document.getElementById('user-input').value;
    const responseDiv = document.getElementById('chat-output');

    if (!userInput) {
        responseDiv.innerText = 'Please enter some text.';
        return;
    }

    try {
        const response = await fetch('/qa', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text: userInput }),
        });


        if (response.ok) {
            const responseData = await response.json();
            console.log('Response data:', responseData); // Add this line

            const processedText = responseData.processed_text;
            responseDiv.innerText = processedText;

        } else {
            console.log('Error response:', response); // Add this line
            responseDiv.innerText = 'Error processing the text.';
        }
    } catch (error) {
        console.error('Error:', error);
        responseDiv.innerText = 'Python Error processing the text.';
    }
});
