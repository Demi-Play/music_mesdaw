// src/pages/Project.js
import React, { useEffect, useState } from 'react';
import { Typography } from '@mui/material';
import { useParams } from 'react-router-dom';
import axios from 'axios';

const Project = () => {
    const { projectId } = useParams();
    const [project, setProject] = useState(null);

    useEffect(() => {
        const fetchProject = async () => {
            try {
                const response = await axios.get(`http://127.0.0.1:8000/api/daw/project/${projectId}/`);
                setProject(response.data);
            } catch (error) {
                console.error('Error fetching project:', error);
            }
        };

        fetchProject();
    }, [projectId]);

    return (
        <div>
            {project ? (
                <>
                    <Typography variant="h4" gutterBottom>
                        Project: {project.name}
                    </Typography>
                    <Typography variant="body1">
                        Tracks: {JSON.stringify(project.tracks)}
                    </Typography>
                    <Typography variant="body1">
                        Mixer Settings: {JSON.stringify(project.mixer_settings)}
                    </Typography>
                </>
            ) : (
                <Typography variant="body1">Loading project...</Typography>
            )}
        </div>
    );
};

export default Project;
