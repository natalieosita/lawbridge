import React from 'react';
import { Link } from 'react-router-dom';
import styled from 'styled-components';
import logo from '../../public/assets/logo.png';
import logoutUser from '../utils/authUtils';

const Navbar = styled.nav`
  display: flex;
  justify-content: space-between;
  background: ${({ theme }) => theme.colors.primary};
  padding: 1rem 2rem;
  align-items: center;
`;

const NavSection = styled.div`
  display: flex;
  align-items: center;
  gap: 1.5rem;
`;

const NavLinks = styled.div`
  display: flex;
  gap: 1rem;

  a, button {
    color: white;
    background: none;
    border: none;
    font-weight: 500;
    cursor: pointer;
    text-decoration: none;
  }
`;

const ThemeButton = styled.button`
  background: none;
  border: 1px solid white;
  color: white;
  padding: 0.4rem 0.8rem;
  border-radius: 4px;
  cursor: pointer;
  font-size: 0.85rem;
`;

const Header = ({ toggleTheme, isDarkMode }) => {
  const isAuthenticated = !!localStorage.getItem('token');

  return (
    <Navbar>
      <Link to="/"><img src={logo} alt="LawBridge" height={40} /></Link>
      <NavSection>
        <NavLinks>
          <Link to="/cases">Cases</Link>
          {isAuthenticated ? (
            <>
              <Link to="/dashboard">Dashboard</Link>
              <button onClick={logoutUser}>Logout</button>
            </>
          ) : (
            <>
              <Link to="/login">Login</Link>
              <Link to="/register">Register</Link>
            </>
          )}
        </NavLinks>
        <ThemeButton onClick={toggleTheme}>
          {isDarkMode ? '🌞 Light Mode' : '🌙 Dark Mode'}
        </ThemeButton>
      </NavSection>
    </Navbar>
  );
};

export default Header;