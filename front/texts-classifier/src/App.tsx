import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import MainPage from './pages/MainPage';
import SignInPage from './pages/LoginPage';

export default function App() {
    return (
        <div className="App">
            <Header />

            <BrowserRouter>
                <Routes>
                    <Route path="/" element={<SignInPage />} />
                    <Route path="/signin" element={<SignInPage />} />
                    <Route path="/home" element={<MainPage />} />
                </Routes>
            </BrowserRouter>

            <Footer />
        </div>
    );
}
