import React, { useState } from "react";
import {
    Button,
    Link,
    TextField,
    Box, // Added Box for spacing
} from "@mui/material";
import { DataGrid } from '@mui/x-data-grid';
import indicatorsImage from "../public/indicators.png";
import confusionMatrixImage from "../public/confusion_matrix.png";
import '../styles/ModelPage.css';

const ModelPage: React.FC = () => {
    const [trainingData, setTrainingData] = useState<{ id: string; text: string; category: number }[]>([]);
    const [testingData, setTestingData] = useState<{ id: string; text: string; category: number }[]>([]);
    const [seeTrainingData, setSeeTrainingData] = useState(false);
    const [seeTestingData, setSeeTestingData] = useState(false);

    const fetchData = async (url: string, setData: React.Dispatch<React.SetStateAction<{ id: string; text: string; category: number }[]>>) => {
        const response = await fetch(url);
        const data = await response.json();
        setData(data);
    };

    const columns = [
        { field: 'text', headerName: 'Texto', flex: 1 },
        { field: 'category', headerName: 'Categoría', flex: 1 },
    ];

    return (
        <Box p={2}> {/* Added Box for spacing */}
            {/* Back to Home Button */}
            <Link href="/home">
                <Button component="a" variant="contained" id="back-home-button">
                    Volver al inicio
                </Button>
            </Link>

            {/* Model Description TextField */}
            <TextField
                multiline
                rows={4}
                fullWidth
                variant="outlined"
                margin="normal"
                label="Descripción del modelo"
                value={`La regresión logística es un método que ajusta una función logística a los datos, con base en eso determina la probabilidad de que cada dato pertenezca a una categoría y teniendo en cuenta dichas probabilidades asigna la clasificación.

Es especialmente útil en caso de que haya relaciones lineales entre los datos (lo cual no se sabe de antemano) e intenta maximizar la probabilidad de que la clasificación sea correcta. Además, provee dicha probabilidad. Por ende, se complementa con los demás modelos que se eligieron para probar, que eran Naive Bayes y Red Neuronal. Al evaluar los tres modelos, se encontró que la regresión logística es la que mejor clasifica los textos. Los indicadores de desempeño del modelo se muestran en las gráficas inferiores. Recuérdese el significado de cada uno:
• Precisión (accuracy): Indica qué proporción o porcentaje de los registros fueron clasificados de forma correcta.
• Macro precisión o precisión por clase: Realiza un promedio de la precisión que tiene el modelo para cada clasificación. Permite evaluar si el modelo es bueno clasificando textos en el ODS 6, en el 7 y en el 16, o si solo es bueno clasificando textos en ODS específico.
• Recall o sensibilidad: Mide la tasa de “verdaderos positivos” clasificados correctamente, es decir, qué proporción de los textos fueron asignados su ODS correcta. Se complementa con la precisión, pues puede pasar que un modelo sea muy sensible pero poco preciso (por ejemplo, si clasifica todos los textos como el ODS 6, va a tener una alta sensibilidad a la clase del ODS 6 pero una mala precisión).
• Puntaje F1: Teniendo en cuenta que la precisión y la sensibilidad se complementan, el puntaje F1 los contempla ambos, siendo su promedio ponderado.`}
            />

            {/* Image: Graph */}
            <img src={indicatorsImage} alt="Indicators Graph" />

            {/* Image: Confusion Matrix */}
            <img src={confusionMatrixImage} alt="Confusion Matrix" />
            <br />
            {/* Button to fetch training data */}
            <Button
                variant="contained"
                onClick={() => {
                    fetchData("http://localhost:8000/excerpts/train", setTrainingData);
                    setSeeTrainingData(true);
                    setSeeTestingData(false);
                }}
                id="training-data-button"
            >
                Ver datos de entrenamiento
            </Button>

            {/* Horizontal spacing */}
            &nbsp;&nbsp;

            {/* Button to fetch testing data */}
            <Button
                variant="contained"
                onClick={() => {
                    fetchData("http://localhost:8000/excerpts/test", setTestingData);
                    setSeeTrainingData(false);
                    setSeeTestingData(true);
                }}
                id="testing-data-button"
            >
                Ver datos de pruebas
            </Button>

            {/* Display training or testing data in a DataGrid */}
            {seeTrainingData || seeTestingData ? (
                <div style={{ height: 400, width: '100%' }}>
                    <DataGrid
                        rows={seeTrainingData ? trainingData : testingData}
                        columns={columns}
                    />
                </div>
            ) : null}
        </Box>
    );
};

export default ModelPage;
