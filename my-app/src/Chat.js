import React from 'react';
import './Chat.css';
import ChatBubble from './ChatBubble.js';

function Chat({ BotMessages, UserMessages }) {
    //component to display both the BotMessages (response + source) and the (User Questions)
    let chat_index = 1; //initialize index for bot messages, index 0 is the welcome message
    console.log("BotMessages", BotMessages)
    return (
        <main className="Chat">
        <div className="BotOutput">
          <ChatBubble key={0} message={BotMessages[0]} />
        </div>
        {UserMessages.map((message, index) => (
          <div key={index}>
            <div className="UserInput">
              <ChatBubble key={index} message={message} />
            </div>
            <div className="BotOutput">
              <ChatBubble key={index * 2} message={BotMessages[index * 2 +1]} />
              <ChatBubble key={index * 2 + 1} message={BotMessages[(index+1) * 2 ]} />
            </div>
          </div>
        ))}
      </main>      
    );
  }
  


export default Chat;
/* {while (chat_index < UserMessages.length) {
          <div className="BotOutput">
            <ChatBubble key={chat_index * 2} message={BotMessages[chat_index * 2]} />
            <ChatBubble key={chat_index * 2 + 1} message={BotMessages[chat_index * 2 + 1]} />
          </div>
          <div className="UserInput">
            <ChatBubble key={chat_index} message={UserMessages[chat_index]} />
          </div>
          chat_index++;
        }} */