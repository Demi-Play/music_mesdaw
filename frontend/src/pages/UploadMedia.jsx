// src/pages/UploadMedia.js
import React, { useState } from 'react';
import { Typography, Button, TextField } from '@mui/material';
import axios from 'axios';

const UploadMedia = () => {
    const [file, setFile] = useState(null);
    const [metadata, setMetadata] = useState('');

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    const handleUpload = async () => {
        const formData = new FormData();
        formData.append('file', file);
        formData.append('metadata', JSON.stringify({ description: metadata }));

        try {
            const response = await axios.post('http://127.0.0.1:8000/api/media/upload/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });
            alert('File uploaded successfully: ' + response.data.message);
        } catch (error) {
            console.error('Error uploading file:', error);
            alert('Error uploading file');
        }
    };

    return (
        <div>
            <Typography variant="h4" gutterBottom>
                Upload Media File
            </Typography>
            <input type="file" onChange={handleFileChange} />
            <TextField
                label="Metadata"
                variant="outlined"
                fullWidth
                margin="normal"
                value={metadata}
                onChange={(e) => setMetadata(e.target.value)}
            />
            <Button variant="contained" onClick={handleUpload}>
                Upload
            </Button>
        </div>
    );
};

export default UploadMedia;
