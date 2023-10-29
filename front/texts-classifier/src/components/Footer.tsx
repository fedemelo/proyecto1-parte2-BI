import { Link, Typography } from "@mui/material";
import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/Footer.css'

export default function Footer() {
    return <Typography variant="body2" color="text.secondary" align="center">
        {'Copyright © '}
        <Link color="inherit" href="#">
            Clasificador de textos en ODS 6, 7 o 16. Por Federico Melo y Shadith Pérez.
        </Link>{' '}
        {new Date().getFullYear()}
        {'.'}
    </Typography>
}