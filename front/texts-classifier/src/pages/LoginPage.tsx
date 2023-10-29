import React from 'react';
import { Form, Button, Container } from 'react-bootstrap';
import {
    Grid,
    Paper,
    Avatar,
    Typography,
    Link,
    Box
} from '@mui/material';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import '../styles/LoginPage.css'

export default function LoginPage() {
    return <Grid container component="main" sx={{ height: '80vh' }}>
        <Grid
            item
            xs={false}
            sm={4}
            md={7}
            sx={{
                backgroundImage: 'url(https://source.unsplash.com/random?wallpapers)',
                backgroundRepeat: 'no-repeat',
                backgroundSize: 'cover',
                backgroundPosition: 'center',
            }}
        />
        <Grid item xs={12} sm={8} md={5} component={Paper} elevation={6} square>
            <Box
                sx={{ my: 8, mx: 4, display: 'flex', flexDirection: 'column', alignItems: 'center' }}
            >
                <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
                    <LockOutlinedIcon />
                </Avatar>
                <Typography component="h1" variant="h5">
                    Ingresar
                </Typography>
            </Box>
            <Box
                sx={{ my: 8, mx: 4, display: 'flex', flexDirection: 'column' }}
            >


                <LoginForm />
                <Link href="#" variant="body2">
                    Olvidé la contraseña
                </Link>
            </Box>
        </Grid>
    </Grid>
}

const LoginForm = () => {

    const [formValues, setFormValues] = React.useState({
        username: '',
        password: '',
    })

    const [formValueIsInvalid, setFormValueIsInvalid] = React.useState({
        userName: false,
        password: false,
    })

    const clickSubmit = async () => {

        const response = await fetch('http://localhost:8000/logins', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formValues),
        })
        const data = await response.json()

        if (data.username) {
            window.location.href = "/home"
        } else {
            setFormValueIsInvalid({
                userName: true,
                password: true,
            })
        }
    }

    const clickCancel = () => {
        setFormValues({
            username: '',
            password: '',
        })
    }

    return <Form id="formBox">
        <Form.Group>
            <Form.Label className="loginText">Nombre de usuario</Form.Label>
            <Form.Control
                id='userName'
                onChange={(event) => setFormValues({
                    ...formValues,
                    username: event.target.value
                })}
                value={formValues.username}
                isInvalid={formValueIsInvalid.userName}
            />
        </Form.Group>
        <Form.Group>
            <Form.Label className="loginText">Contraseña</Form.Label>
            <Form.Control
                id='password'
                type="password"
                onChange={(event) => setFormValues({
                    ...formValues,
                    password: event.target.value
                })}
                value={formValues.password}
                isInvalid={formValueIsInvalid.password}
            />
        </Form.Group>
        <Container id="loginButtonsText">
            <Container id="loginButtons">
                <Button id="submitButton" variant="success btn-lg" onClick={clickSubmit}>
                    Ingresar
                </Button>
                <Button id="cancelButton" variant="danger btn-lg" onClick={clickCancel}>
                    Cancelar
                </Button>
            </Container>
            <Form.Text id="errorAuth" className='loginText'>{(formValueIsInvalid.userName || formValueIsInvalid.password) ? "Error de autenticación. Revise sus credenciales" : ""}</Form.Text>
        </Container>
    </Form>

}
