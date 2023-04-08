import React, { useState } from "react";

function Search({ setBotMessages, setUserMessages }) {
  const [searchTerm, setSearchTerm] = useState("");

  const handleSearchInputChange = (event) => {
    setSearchTerm(event.target.value);
  };

  const handleSearchSubmit = (event) => {
    event.preventDefault();
    // Add code here to handle search submission and update chat messages
    setUserMessages((chatMessages) => [...chatMessages, searchTerm]);
    const formData = new FormData();
    formData.append("searchTerm", searchTerm);
    //send POST request with searchTerm as body
    const backendURL = "http://localhost:5006";
    fetch("/qa", {
        method: "POST",
        body: formData
      })
        .then((response) => {console.log("response", response); return response.json();})
        .then((data) => {
            setBotMessages((BotMessages) => {console.log('data: ', data);return [...BotMessages, data['answer'], data['source_documents']]});
        })
        .catch((error) => {
          console.error("Error uploading question:", error);
        });
  };

  return (
    <form onSubmit={handleSearchSubmit}>
      <div className="search-bar">
        <input
          type="text"
          name="search-input"
          placeholder="Search..."
          value={searchTerm}
          onChange={handleSearchInputChange}
        />
        <button type="submit"><i className="fas fa-search"></i></button>
      </div>
    </form>
  );
}

export default Search;
