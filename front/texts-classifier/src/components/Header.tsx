import {
    AppBar,
    Toolbar,
    Box,
    Typography
} from '@mui/material';
import '../styles/Header.css';
import logoImage from '../public/LogoODS.jpg';

export default function Header() {
    return (
        <Box id="headerContainer">
            <AppBar position="static" style={{ background: 'white'}}>
                <Toolbar >
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', width: '100%' }}>
                    <img src={logoImage} id="headerImage" alt="" />
                    </div>
                </Toolbar>
            </AppBar>
            <Typography variant="h5" id="headerTitle">
                Se clasifican los textos en tres ODS.
            </Typography>
        </Box >
    );
}