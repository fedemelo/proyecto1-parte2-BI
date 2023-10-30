import React from 'react';
import { Form, Button, Container } from 'react-bootstrap';
import {
    Grid,
    Paper,
    Avatar,
    Typography,
    Link,
    Box,
    TextField,
    FormControlLabel,
    Checkbox
} from '@mui/material';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import '../styles/LoginPage.css'

export default function LoginPage() {

    const [formValues, setFormValues] = React.useState({
        username: '',
        password: '',
    })

    const handleChange = (e: { target: { name: any; value: any; }; }) => {
        const { name, value } = e.target;
        setFormValues((prevValues) => ({
            ...prevValues,
            [name]: value,
        }));
    };

    const clickSubmit = async () => {

        setFormValues((prevValues) => ({
            ...prevValues,
            password: '',
        }));

        const response = await fetch('http://localhost:8000/logins', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formValues),
        });

        if (response.status === 201) {
            window.location.href = '/home';
        }
        else {
            alert('Usuario o contraseña incorrectos');
        }
    }

    return <Grid container component="main" sx={{ height: '60vh' }}>
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
                sx={{
                    my: 8,
                    mx: 4,
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                }}
            >
                <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
                    <LockOutlinedIcon />
                </Avatar>
                <Typography component="h1" variant="h5">
                    Sign in
                </Typography>
                <Box component="form" sx={{ mt: 1 }}>
                    <TextField
                        margin="normal"
                        required
                        fullWidth
                        id="email"
                        label="Email Address"
                        name="username"  // Change "email" to "username"
                        autoComplete="email"
                        autoFocus
                        value={formValues.username}  // Add this line
                        onChange={handleChange}     // Add this line
                    />
                    <TextField
                        margin="normal"
                        required
                        fullWidth
                        name="password"
                        label="Password"
                        type="password"
                        id="password"
                        autoComplete="current-password"
                        value={formValues.password}  // Add this line
                        onChange={handleChange}     // Add this line
                    />
                    <FormControlLabel
                        control={<Checkbox value="remember" color="primary" />}
                        label="Remember me"
                    />
                    <Button
                        type="submit"
                        variant="contained"
                        onClick={clickSubmit}
                    >
                        Sign In
                    </Button>
                    <Grid container>
                        <Grid item xs>
                            <Link href="#" variant="body2">
                                Forgot password?
                            </Link>
                        </Grid>
                        <Grid item>
                            <Link href="#" variant="body2">
                                {"Don't have an account? Sign Up"}
                            </Link>
                        </Grid>
                    </Grid>
                </Box>
            </Box>
        </Grid>
    </Grid>
}
