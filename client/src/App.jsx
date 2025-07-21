import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import PrivateRoute from './components/PrivateRoute';
import Home from './pages/Home';
import Login from './pages/Login';
import Register from './pages/Register';
import Dashboard from './pages/Dashboard';
import Cases from './pages/Cases';
import { ThemeProvider } from 'styled-components';
import { lightTheme, darkTheme } from './styles/theme';
import GlobalStyle from './styles/global';

const App = () => {
  const getSystemPrefersDark = () =>
    window.matchMedia &&
    window.matchMedia('(prefers-color-scheme: dark)').matches;

  const [isDarkMode, setIsDarkMode] = useState(() => {
    const storedTheme = localStorage.getItem('theme');
    return storedTheme === 'dark' || (!storedTheme && getSystemPrefersDark());
  });

  const toggleTheme = () => {
    const nextMode = !isDarkMode;
    setIsDarkMode(nextMode);
    localStorage.setItem('theme', nextMode ? 'dark' : 'light');
  };

  useEffect(() => {
    const stored = localStorage.getItem('theme');
    if (stored !== 'dark' && stored !== 'light') {
      const prefersDark = getSystemPrefersDark();
      setIsDarkMode(prefersDark);
      localStorage.setItem('theme', prefersDark ? 'dark' : 'light');
    }
  }, []);

  return (
    <ThemeProvider theme={isDarkMode ? darkTheme : lightTheme}>
      <GlobalStyle />
      <Router>
        <Header toggleTheme={toggleTheme} isDarkMode={isDarkMode} />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route
            path="/dashboard"
            element={<PrivateRoute><Dashboard /></PrivateRoute>}
          />
          <Route
            path="/cases"
            element={<PrivateRoute><Cases /></PrivateRoute>}
          />
        </Routes>
        <Footer />
      </Router>
    </ThemeProvider>
  );
};

export default App;