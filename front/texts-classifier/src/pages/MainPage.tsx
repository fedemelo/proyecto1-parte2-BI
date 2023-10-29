import React, { useState } from "react";
import {
    Typography,
    Grid,
    Button,
    TextField,
} from "@mui/material";
import ClassifyExcel from "../components/ClassifyExcel";
import ClassifyText from "../components/ClassifyText";

import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/MainPage.css';


const TextDisplay: React.FC<{ texts: { text: string; id: string; category: number }[] }> = ({ texts }) => (
    <div>
        <hr />
        <h2>Textos clasificados como el ODS {texts[0].category}</h2>
        {texts.map((textEntry) => (
            <div key={textEntry.id}>
                <Typography variant="body1">{textEntry.text}</Typography>
                <hr />
            </div>
        ))}
    </div>
);

// MainPage component
const MainPage: React.FC = () => {
    const [selectedCategory, setSelectedCategory] = useState<number | null>(null);
    const [texts, setTexts] = useState<{ text: string; id: string; category: number }[]>([]);

    const handleObjectiveClick = async (category: number) => {
        const response = await fetch(`http://localhost:8000/excerpts/ods/${category}`);
        const data = await response.json();

        setTexts(data);
        setSelectedCategory(category);
    };

    return (
        <Grid container spacing={2} id="main-grid">
            <Objective num={6} onClick={() => handleObjectiveClick(6)} />
            <Objective num={7} onClick={() => handleObjectiveClick(7)} />
            <Objective num={16} onClick={() => handleObjectiveClick(16)} />
            <Grid md={6} id="classify-text-grid">
                <ClassifyText />
            </Grid>
            <Grid md={6} id="classify-excel-grid">
                <ClassifyExcel />
            </Grid>
            <Grid md={12} id="show-texts">
                {selectedCategory !== null && <TextDisplay texts={texts} />}
            </Grid>
        </Grid>
    );
};

// Objective component
const Objective: React.FC<{ num: number; onClick: () => void }> = ({ num, onClick }) => (
    <Grid md={4}>
        <Button variant="contained" onClick={onClick}>
            ODS {num}
        </Button>
    </Grid>
);

export default MainPage;