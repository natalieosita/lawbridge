import React, { useState } from 'react';
import useLogin from '../api/useLogin';
import { useNavigate } from 'react-router-dom';

const Login = () => {
  const [form, setForm] = useState({ email: '', password: '' });
  const navigate = useNavigate();
  const loginMutation = useLogin();

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await loginMutation.mutateAsync(form);
      localStorage.setItem('token', res.data.token);
      navigate('/dashboard');
    } catch {
      alert('Login failed');
    }
  };

  return (
    <form onSubmit={handleSubmit} style={{ padding: '2rem' }}>
      <h2>Login</h2>
      <input name="email" type="email" placeholder="Email" onChange={handleChange} required /><br /><br />
      <input name="password" type="password" placeholder="Password" onChange={handleChange} required /><br /><br />
      <button type="submit">Login</button>
    </form>
  );
};

export default Login;