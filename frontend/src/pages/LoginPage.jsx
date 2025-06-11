import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import './LoginPage.css';
import ToolBar from '../elements/ToolBar';

const LoginPage = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const { login } = useAuth();
  const navigate = useNavigate();
  
  const handleLogin = () => {
    fetch('/auth/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, password })
    })
    .then(response => {
      if (response.ok) {
        login();
        navigate('/dashboard');
      } else {
        alert('Invalid credentials');
      }
    })
    .catch(error => {
      console.error('Login error:', error);
      alert('Something went wrong. Please try again.');
    });
  };

  return (
    <div className="loginpage">
      <ToolBar />
      <div className="login-box">
        <h1 className='login'>Login</h1>
        <input
          type="text"
          className="credentials-input"
          placeholder="Enter username..."
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <input
          type="password"
          className="credentials-input"
          placeholder="Enter password..."
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button className="login-button" onClick={handleLogin}>
          Login
        </button>
      </div>
    </div>
  );
};

export default LoginPage;