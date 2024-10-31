// src/pages/Home.js
import React from 'react';
import { Typography } from '@mui/material';

const Home = () => {
    return (
        <div>
            <Typography variant="h4" gutterBottom>
                Welcome to the Music Messenger
            </Typography>
            <Typography variant="body1">
                This is a platform for sharing messages and media files.
            </Typography>
        </div>
    );
};

export default Home;
