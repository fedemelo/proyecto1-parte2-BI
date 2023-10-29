import { Link, Typography } from "@mui/material";
import '../styles/Footer.css';

export default function Footer() {
    return (
        <div className="container">
            <div className="content">
                {/* Contenido de tu página */}
            </div>
            <div className="footer">
                <Typography variant="body2" color="text.secondary">
                    {'Copyright © '}
                    <Link color="inherit" href="#">
                        Clasificador de textos en ODS 6, 7 o 16. Por Federico Melo y Shadith Pérez.
                    </Link>{' '}
                    {new Date().getFullYear()}
                    {'.'}
                </Typography>
            </div>
        </div>
    );
}
