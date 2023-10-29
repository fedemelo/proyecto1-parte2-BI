import React, { useState } from 'react';
import {
    Typography,
    Button,
    TextField,
} from '@mui/material';
import '../styles/ClassifyText.css';
 
const ClassifyText: React.FC = () => {
    const [message, setMessage] = useState<string>('');
    const [category, setCategory] = useState<string>('');

    const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setMessage(event.target.value);
    };

    const handleSendClick = async () => {

        if (!message) {
            return;
        }

        const response = await fetch('http://localhost:8000/excerpts', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                "text": message
            }),
        })
        const data = await response.json()

        if (data.category) {
            setCategory(data.category)
        } else {
            setCategory('No se pudo clasificar')
        }
    };

    return (
        <div>
            <TextField
                 id="text-to-classify"
                 label="Ingrese el texto a clasificar en el ODS 6, 7 o 16"
                 variant="outlined"
                 value={message}
                 onChange={handleInputChange}
            />

            <Button
                id="classify-button"
                variant="contained"
                onClick={handleSendClick}>
                Clasificar
            </Button>


            <Typography
                id="classification-result"
                variant="h1"            >
                Clasificación: {category !== "" ? "ODS " + category : "No se ha ingresado un texto"}
            </Typography>

        </div>
    );
};

export default ClassifyText;