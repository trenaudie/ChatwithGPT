import React from 'react';
import './Chat.css';
import ChatBubble from './ChatBubble.js';

function Chat({ chatMessages, setChatMessages }) {
  const addChatMessage = (message) => {
    setChatMessages([...chatMessages, message]);
  };

  return (
    <main className="Chat">
      <div className="ChatOutput">
        {chatMessages.map((message, index) => (
          <ChatBubble key={index} message={message} />
        ))}
      </div>
    </main>
  );
}

export default Chat;
