document.getElementById('upload-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const fileInput = document.getElementById('document');
    const formData = new FormData();
    formData.append('document', fileInput.files[0]);

    try {
        const response = await fetch('/upload', {
            method: 'POST',
            body: formData,
        });

        const responseDiv = document.getElementById('upload-response');

        if (response.ok) {
            responseDiv.innerText = 'File uploaded and saved.';
            fileInput.value = ''; // Clear the input field
        } else {
            responseDiv.innerText = 'Error uploading the file.';
        }
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('upload-response').innerText = 'An error occurred while uploading the file.';
    }
});
