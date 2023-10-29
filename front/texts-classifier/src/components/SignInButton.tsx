import { Nav } from 'react-bootstrap';
import Button from '@mui/material/Button';

export default function SignInButton() {
    return (
        <Nav.Link href='/signin'>
            <Button variant="contained">
                {"Ingresar"}
            </Button>
        </Nav.Link>
    )
}