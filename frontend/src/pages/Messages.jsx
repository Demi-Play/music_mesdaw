// src/pages/Messages.js
import React, { useEffect, useState } from 'react';
import { Typography, List, ListItem } from '@mui/material';
import axios from 'axios';

const Messages = () => {
    const [messages, setMessages] = useState([]);

    useEffect(() => {
        const fetchMessages = async () => {
            try {
            alert(localStorage.getItem('user'))
            const response = await axios.get('http://127.0.0.1:8000/api/messages/');
                setMessages(response.data);
            } catch (error) {
                console.error('Error fetching messages:', error);
            }
        };

        fetchMessages();
    }, []);

    return (
        <div>
            <Typography variant="h4" gutterBottom>
                Messages
            </Typography>
            <List>
                {messages.map((message, index) => (
                    <ListItem key={index}>
                        <Typography variant="body1">
                            <strong>{message.sender}:</strong> {message.text}
                        </Typography>
                    </ListItem>
                ))}
            </List>
        </div>
    );
};

export default Messages;
