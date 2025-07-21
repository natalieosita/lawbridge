import React, { useState } from 'react';
import useRegister from '../api/useRegister';
import { useNavigate } from 'react-router-dom';

const Register = () => {
  const [form, setForm] = useState({ name: '', email: '', password: '' });
  const navigate = useNavigate();
  const registerMutation = useRegister();

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await registerMutation.mutateAsync(form);
      localStorage.setItem('token', res.data.token);
      navigate('/dashboard');
    } catch {
      alert('Registration failed');
    }
  };

  return (
    <form onSubmit={handleSubmit} style={{ padding: '2rem' }}>
      <h2>Register</h2>
      <input name="name" placeholder="Full Name" onChange={handleChange} required /><br /><br />
      <input name="email" type="email" placeholder="Email" onChange={handleChange} required /><br /><br />
      <input name="password" type="password" placeholder="Password" onChange={handleChange} required /><br /><br />
      <button type="submit">Sign Up</button>
    </form>
  );
};

export default Register;