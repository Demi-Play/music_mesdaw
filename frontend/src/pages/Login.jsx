// src/components/Login.js
import React, { useState } from 'react';
import axios from 'axios';
import { TextField, Button, Typography, Container } from '@mui/material';
import { useNavigate  } from 'react-router-dom';

const Login = () => {
    const history = useNavigate();
    const [credentials, setCredentials] = useState({
        username: '',
        password: '',
    });
    const [error, setError] = useState('');

    const handleChange = (e) => {
        const { name, value } = e.target;
        setCredentials({ ...credentials, [name]: value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('http://127.0.0.1:8000/api/login/', credentials);
            localStorage.setItem('token', response.data.token);
            localStorage.setItem('user', response.data.user);
            history('/messages');
        } catch (error) {
            setError('Ошибка входа: неверные учетные данные');
            console.error('Login error', error);
        }
    };

    return (
        <Container style={{display: 'flex', alignItems: 'center', flexDirection: 'column'}}>
            <Typography variant="h4" gutterBottom>
                Вход
            </Typography>
            {error && <Typography color="error">{error}</Typography>}
            <form onSubmit={handleSubmit}>
                <TextField
                    name="username"
                    onChange={handleChange}
                    label="Имя пользователя"
                    variant="outlined"
                    fullWidth
                    required
                    margin="normal"
                />
                <TextField
                    name="password"
                    type="password"
                    onChange={handleChange}
                    label="Пароль"
                    variant="outlined"
                    fullWidth
                    required
                    margin="normal"
                />
                <Button type="submit" variant="contained" color="primary">
                    Войти
                </Button>
            </form>
        </Container>
    );
};

export default Login;
