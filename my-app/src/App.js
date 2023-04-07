import React, { useState } from 'react';
import './App.css';
import NavigationBar from './NavigationBar';
import Chat from './Chat';
import Search from './Search';

function App() {
  const [sources, setSources] = useState(['source1', 'source2', 'source3']);
  const [chatMessages, setChatMessages] = useState(["Hi there! I'm your friendly chatbot. To get started, please upload a PDF document containing the information you'd like to chat about. Simply click the 'Upload Document' button to select your file, and then we can begin our chat. Let me know if you have any questions!"]);

  return (
    <div className="App">
      <NavigationBar sources={sources} setSources={setSources} />
      <Chat chatMessages={chatMessages} setChatMessages={setChatMessages} />
      <Search setChatMessages={setChatMessages} />
    </div>
  );
}

export default App;
