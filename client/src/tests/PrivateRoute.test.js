import { render, screen } from '@testing-library/react';
import PrivateRoute from '../components/PrivateRoute';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

jest.mock('../utils/tokenUtils', () => () => true);

describe('PrivateRoute component', () => {
  test('renders children if token is valid', () => {
    localStorage.setItem('token', 'test-jwt');

    render(
      <BrowserRouter>
        <Routes>
          <Route
            path="/"
            element={
              <PrivateRoute>
                <h1>Protected Content</h1>
              </PrivateRoute>
            }
          />
        </Routes>
      </BrowserRouter>
    );

    expect(screen.getByText(/Protected Content/i)).toBeInTheDocument();
  });

  test('redirects if token missing or expired', () => {
    localStorage.removeItem('token');

    render(
      <BrowserRouter>
        <Routes>
          <Route
            path="/"
            element={
              <PrivateRoute>
                <h1>Protected</h1>
              </PrivateRoute>
            }
          />
          <Route path="/login" element={<h1>Login Page</h1>} />
        </Routes>
      </BrowserRouter>
    );

    expect(screen.getByText(/Login Page/i)).toBeInTheDocument();
  });
});