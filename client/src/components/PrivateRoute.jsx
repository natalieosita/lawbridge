import React from 'react';
import { Navigate } from 'react-router-dom';
import isTokenExpired from '../utils/tokenUtils';

const PrivateRoute = ({ children }) => {
  const token = localStorage.getItem('token');
  return token && !isTokenExpired(token) ? children : <Navigate to="/login" />;
};

export default PrivateRoute;