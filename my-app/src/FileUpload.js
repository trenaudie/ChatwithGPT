import React from "react";

function FileUpload() {
  const handleFileUpload = (event) => {
    const file = event.target.files[0];
    const formData = new FormData();
    formData.append("sourceInput", file);

    fetch("/upload", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("File upload successful");
        // Add code here to handle the response data
      })
      .catch((error) => {
        console.error("Error uploading file:", error);
      });
  };

  return (
    <div>
      <label htmlFor="file-upload">Choose a file:</label>
      <input type="file" name="sourceInput" id="file-upload" onChange={handleFileUpload} />
    </div>
  );
}

export default FileUpload;
