import React from 'react';
import './NavigationBar.css';
import './FileUpload.js'
import FileUpload from './FileUpload.js';
function NavigationBar({ Sources, setSources }) {
  const handleSourceSubmit = (event) => {
    event.preventDefault();
    const newSource = event.target.sourceInput.value;
    setSources([...Sources, newSource]);
    event.target.sourceInput.value = '';
  };

  return (
    <nav className="NavigationBar">
      <form onSubmit={handleSourceSubmit}>
        <label htmlFor="sourceInput">Sources:</label>
        <ul>
          {Sources.map((source, index) => (
            <li key={index}>{source}</li>
          ))}
        </ul>
        <FileUpload/>
        <button type="submit">Add Source</button>
      </form>
    </nav>
  );
}


export default NavigationBar;
