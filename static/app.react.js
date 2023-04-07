import React, { useState } from "react";
import "./App.css";

function App() {
  const [searchInput, setSearchInput] = useState("");
  const [chatOutput, setChatOutput] = useState("");

  const handleSearchInputChange = (event) => {
    setSearchInput(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    // Add code here to handle form submission and update chatOutput state
  };

  return (
    <div className="App">
      <nav>
        <form id="upload-form">
          <label htmlFor="document">Upload a document:</label>
          <input type="file" name="document" id="document" accept=".pdf,.doc,.docx,.txt" />
          <button type="submit">Upload Document</button>
        </form>
        <div id="upload-response"></div>
      </nav>
      <main>
        <form id="text-form" onSubmit={handleSubmit}>
          <div className="search-bar">
            <label htmlFor="search-input">Question:</label>
            <input
              type="text"
              name="search-input"
              id="search-input"
              value={searchInput}
              placeholder="Search..."
              onChange={handleSearchInputChange}
            />
            <button type="submit"><i className="fas fa-search"></i></button>
          </div>
        </form>
        <div className="chat-output">
          <div className="chat-bubble">
            <p>{chatOutput}</p>
          </div>
        </div>
      </main>
    </div>
  );
}

export default App;
