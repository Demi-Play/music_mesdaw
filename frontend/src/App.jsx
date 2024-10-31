// src/App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Messages from './pages/Messages';
import UploadMedia from './pages/UploadMedia';
import Project from './pages/Project';
import Navbar from './components/Navbar';
import Register from './pages/Register';
import Login from './pages/Login';
import './App.css';
import NavbarUnReg from './components/NavbarUnReg';

const App = () => {
    return (
        <Router>
            <NavbarUnReg />
            <Navbar />
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/register" element={<Register />} />
                <Route path="/login" element={<Login />} />
                <Route path="/logout" element={<Login />} />
                <Route path="/messages" element={<Messages />} />
                <Route path="/upload" element={<UploadMedia />} />
                <Route path="/project/:projectId" element={<Project />} />
            </Routes>
        </Router>
    );
};

export default App;
