import React, { useState } from "react";
import {
    CardActionArea,
    CardContent,
    CardMedia,
    Typography,
    Grid,
    Card,
    CardHeader,
    Avatar,
    Button,
    TextField,
} from "@mui/material";
import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/MainPage.css';

export default function MainPage() {

    const ClassifyText: React.FC = () => {
        const [message, setMessage] = useState<string>('');
        const [category, setCategory] = useState<string>('');

        const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
            setMessage(event.target.value);
        };

        const handleSendClick = async () => {
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
                    label="Ingrese el texto a clasificar en el ODS 6, 7 o 16"
                    variant="outlined"
                    value={message}
                    onChange={handleInputChange}
                />

                <Button variant="contained" color="primary" onClick={handleSendClick}>
                    Clasificar
                </Button>


                <Typography variant="h6" color="primary">
                    Clasificación: {category!="" && "ODS "+category}
                </Typography>

            </div>
        );
    };


    return <Grid container spacing={2}>
        <Objective num={6} />
        <Objective num={7} />
        <Objective num={16} />
        <Grid md={6}>
            <ClassifyText />
        </Grid>
        <Grid md={6}>
            {/* <AddExcel /> */}
        </Grid>
    </Grid>

}


const Objective: React.FC<{ num: number }> = (num) => <Grid md={4}>
    <Button variant="contained">{num.num}</Button>
</Grid>