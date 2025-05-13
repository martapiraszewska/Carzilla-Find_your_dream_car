import React, { useState } from 'react';
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
    // Simulate login logic (replace with actual API call)
    if (username === 'admin' && password === 'password') {
      login();
      navigate('/dashboard'); // Redirect to the dashboard
    } else {
      alert('Invalid credentials');
    }
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