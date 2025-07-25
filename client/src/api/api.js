// client/src/api/api.js
import axios from 'axios';

// Base URL from environment variable
const BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000';

// Create Axios instance
const api = axios.create({
  baseURL: BASE_URL,
  withCredentials: true, // if using cookies/auth
  headers: {
    'Content-Type': 'application/json',
  },
});

// Optional: Interceptors for auth or logging
api.interceptors.request.use(
  (config) => {
    // Example: attach token if available
    const token = localStorage.getItem('authToken');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

api.interceptors.response.use(
  (response) => response,
  (error) => {
    // Optional: global error handling
    console.error('API Error:', error.response?.data || error.message);
    return Promise.reject(error);
  }
);

export default api;