import React, { useState } from 'react';
import {
    Typography,
    Button,
} from '@mui/material';

const ClassifyExcel: React.FC = () => {
    const [file, setFile] = useState<File | null>(null);
    const [classified, setClassified] = useState<number>(0);

    const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        const fileList = event.target.files;

        if (fileList && fileList.length > 0) {
            setFile(fileList[0]);
        }
    };

    const sendClick = () => {
        if (!file) {
            setClassified(3)  // No file selected
        } else {
            setClassified(1)  // Loading!!
        }

        handleSendClick();
    }

    const handleSendClick = async () => {
        if (!file) {
            return;
        }
            
        const formData = new FormData();
        formData.append('file', file);

        const response = await fetch('http://localhost:8000/excerpts/excel', {
            method: 'POST',
            body: formData,
        });

        const data = await response.json();

        if (data) {
            setClassified(2)
        }
    };

    return (
        <div>
            <input
                type="file"
                accept=".xls, .xlsx"
                onChange={handleFileChange}
            />

            <Button
                variant="contained"
                color="primary"
                onClick={sendClick}
            >
                Clasificar Excel
            </Button>

            <Typography
                variant="h6"
                color="primary"
            >
                {classified == 2 ? "Se archivó cada texto del archivo en la categoría correspondiente." :
                 classified == 1 ? "Clasificando los textos..." :
                 classified == 3 ? "No se ha seleccionado un archivo." :
                 ""}
            </Typography>
        </div>
    );
};

export default ClassifyExcel;