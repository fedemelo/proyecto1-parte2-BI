import {
    AppBar,
    Toolbar,
    Box
} from '@mui/material';
import SignInButton from './SignInButton';
import '../styles/Header.css';


export default function Header() {
    return (
        <Box id="headerContainer">
            <AppBar position="static">
                <Toolbar >
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', width: '100%' }}>
                        <h1 id="headerText"><strong>Clasificador de textos en ODS 6, 7 o 16</strong></h1>
                        <SignInButton/>
                    </div>
                </Toolbar>
            </AppBar>
        </Box >
    );
}


