import React from 'react';
import './ChatBubble.css';

function ChatBubble({ message }) {
  return (
    <div className="ChatBubble">
      <p>{message}</p>
    </div>
  );
}

export default ChatBubble;
