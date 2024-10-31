// src/components/Navbar.js
import React from 'react';
import { Link } from 'react-router-dom';
import { AppBar, Toolbar, Typography, Button } from '@mui/material';

const Navbar = () => {
    return (
        <AppBar position="static">
            <Toolbar>
                <Typography variant="h6" sx={{ flexGrow: 1 }}>
                    Music Messenger
                </Typography>
                <Button color="inherit" component={Link} to="/">Home</Button>
                <Button color="inherit" component={Link} to="/messages">Messages</Button>
                <Button color="inherit" component={Link} to="/upload">Upload Media</Button>
                <Button color="inherit" component={Link} to="/logout">Log Out</Button>
            </Toolbar>
        </AppBar>
    );
};

export default Navbar;
