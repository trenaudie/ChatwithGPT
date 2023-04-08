import React, { useState } from 'react';
import './App.css';
import NavigationBar from './NavigationBar';
import Chat from './Chat';
import Search from './Search';

function App() {
  const [Sources, setSources] = useState([""]);
  const [BotMessages, setBotMessages] = useState(["Hi there! I'm your friendly chatbot. To get started, please upload a PDF document containing the information you'd like to chat about. Simply click the 'Upload Document' button to select your file, and then we can begin our chat. Let me know if you have any questions!"]);
  const [UserMessages, setUserMessages] = useState([]);
  //Chat is for displaying -> only pass in the state variable
  //Search is for updating -> pass in the function to update it
  //Navigation Bar creates its own Sources state variable 
  //OR should we have a Sources state variable in App.js and pass it down to Navigation Bar? Yes just in case we want to use it in other components
  return (
  <div className="App">
    <div className="NavigationBar">
      <NavigationBar Sources={Sources} setSources={setSources} />
    </div>
    <div className="MainContainer">
      <div className="Title">MineGPT</div>
      <div className="Chat">
        <Chat BotMessages={BotMessages} UserMessages={UserMessages}/>
      </div>
      <div className="Search">
        <Search setBotMessages={setBotMessages} setUserMessages={setUserMessages}/>
      </div>
    </div>
  </div>


  );
}

export default App;
