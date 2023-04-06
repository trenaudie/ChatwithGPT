document.getElementById('upload-form').addEventListener('submit', async function (event) {
    event.preventDefault();

    const documentInput = document.getElementById('document');
    const formData = new FormData();
    formData.append('document', documentInput.files[0]);

    try {
        const response = await fetch('/upload', {
            method: 'POST',
            body: formData,
        });

        const responseText = await response.text();
        document.getElementById('response').innerText = responseText;

        if (response.ok) {
            // Handle successful upload
            documentInput.value = ''; // Clear the input field
        } else {
            // Handle errors in the response
        }
    } catch (error) {
        // Handle network errors or other issues with the fetch call
        document.getElementById('response').innerText = 'An error occurred while uploading the file.';
    }
});
