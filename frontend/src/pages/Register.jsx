import React, { useState } from 'react';
import axios from 'axios';
import { TextField, Button, Select, MenuItem, TextareaAutosize, Typography, Container } from '@mui/material';

const Register = () => {
    const [formData, setFormData] = useState({
        username: '',
        email: '',
        password: '',
        bio: `My name is ...I'm is ...Was burned in ...`,
        status: 'musician'
    });

    const handleChange = (event) => {
        const { name, value } = event.target;
        setFormData({
            ...formData,
            [name]: value
        });
    };

    const handleRegister = async (event) => {
        event.preventDefault(); // предотвращаем перезагрузку страницы
        try {
            const response = await axios.post('http://127.0.0.1:8000/api/register/', {
                email: formData.email,
                username: formData.username,
                password: formData.password,
            });
            console.log(response.data);
        } catch (error) {
            console.error('Ошибка при регистрации пользователя:', error);
        }
    };

    return (
        <Container style={{display: 'flex', alignItems: 'center', flexDirection: 'column'}}>
            <Typography variant="h4" gutterBottom>
                Регистрация
            </Typography>
            <form onSubmit={handleRegister}>
                <TextField
                    label="Email"
                    name="email"
                    value={formData.email}
                    onChange={handleChange}
                    required
                /><br />
                <TextField
                    label="Username"
                    name="username"
                    value={formData.username}
                    onChange={handleChange}
                    required
                /><br />
                <TextField
                    label="Password"
                    type="password"
                    name="password"
                    value={formData.password}
                    onChange={handleChange}
                    required
                /><br />
                <TextareaAutosize
                    name="bio"
                    onChange={handleChange}
                    placeholder={formData.bio}
                    minRows={3}
                /><br />
                <label htmlFor="status">status - </label>
                <Select
                    name="status"
                    value={formData.status}
                    onChange={handleChange}
                >
                    <MenuItem value="musician" selected>Музыкант</MenuItem>
                    <MenuItem value="artist">Артист</MenuItem>
                    <MenuItem value="producer">Продюсер</MenuItem>
                    <MenuItem value="beatmaker">Битмейкер</MenuItem>
                </Select><br />
                <Button type="submit">Register</Button>
            </form>
        </Container>
    );
};

export default Register;
