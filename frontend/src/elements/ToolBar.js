import React from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import './ToolBar.css';
import logo from '../assets/Carzilla_logo.png';

const ToolBar = () => {
  const { isLogged } = useAuth();
  const navigate = useNavigate();

  const handleHome = () => {
    isLogged ? navigate('/dashboard') : navigate('/');
  };

  const handleLogin = () => {
    navigate('/login');
  };

  const handleProfile = () => {
    navigate('/profile');
  };

  return (
    <div className='toolbar'>
      <div className='toolbar-logo-container'>
        <img src={logo} alt="Carzilla Logo" className='toolbar-logo' />
        <span className='toolbar-title'>Carzilla - Find Your Dream Car</span>
      </div>
      <div className='toolbar-buttons'>
        <button className='toolbar-button' onClick={handleHome}>Home</button>
        {isLogged ? (
          <button className='toolbar-button' onClick={handleProfile}>Profile</button>
        ) : (
          <button className='toolbar-button' onClick={handleLogin}>Login</button>
        )}
      </div>
    </div>
  );
};

export default ToolBar;