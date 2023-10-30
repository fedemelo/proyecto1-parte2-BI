import React, { useEffect, useState } from "react";
import { Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper } from "@mui/material";

const DisplayLog: React.FC = () => {
    const [logData, setLogData] = useState<{ text: string; preprocessed_text: string; category: number }[]>([]);

    useEffect(() => {
        const fetchLogData = async () => {
            try {
                const response = await fetch("http://localhost:8000/excerpts/log");
                const data = await response.json();
                setLogData(data);
            } catch (error) {
                console.error("Error fetching log data:", error);
            }
        };

        fetchLogData();
    }, []);

    return (
        <div>
            <h2>Log de todos los textos clasificados</h2>
            {logData.length > 0 ? (
                <TableContainer component={Paper}>
                    <Table>
                        <TableHead>
                            <TableRow>
                                <TableCell>Texto</TableCell>
                                <TableCell>Texto preprocesado</TableCell>
                                <TableCell>Categoría</TableCell>
                            </TableRow>
                        </TableHead>
                        <TableBody>
                            {logData.map((logEntry, index) => (
                                <TableRow key={index}>
                                    <TableCell>{logEntry.text}</TableCell>
                                    <TableCell>{logEntry.preprocessed_text}</TableCell>
                                    <TableCell>{logEntry.category}</TableCell>
                                </TableRow>
                            ))}
                        </TableBody>
                    </Table>
                </TableContainer>
            ) : (
                <p>No hay datos en el log.</p>
            )}
        </div>
    );
};

export default DisplayLog;
