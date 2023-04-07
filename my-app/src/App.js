import React, { useState } from 'react';
import './App.css';
import NavigationBar from './NavigationBar';
import Chat from './Chat';
import Search from './Search';

function App() {
  const [sources, setSources] = useState([]);
  const [chatMessages, setChatMessages] = useState([]);

  return (
    <div className="App">
      <NavigationBar sources={sources} setSources={setSources} />
      <Chat chatMessages={chatMessages} setChatMessages={setChatMessages} />
      <Search setChatMessages={setChatMessages} />
    </div>
  );
}

export default App;
