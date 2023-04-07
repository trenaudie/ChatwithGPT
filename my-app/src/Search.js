import React, { useState } from "react";

function Search({ setChatMessages }) {
  const [searchTerm, setSearchTerm] = useState("");

  const handleSearchInputChange = (event) => {
    setSearchTerm(event.target.value);
  };

  const handleSearchSubmit = (event) => {
    event.preventDefault();
    // Add code here to handle search submission and update chat messages
    setChatMessages([]);
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
