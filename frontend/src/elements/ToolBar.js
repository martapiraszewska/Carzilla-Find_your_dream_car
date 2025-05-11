import React from 'react';
import { useNavigate } from 'react-router-dom';
import './ToolBar.css';
import logo from '../assets/Carzilla_logo.png';
const ToolBar = () => {
  const navigate = useNavigate();

  const handleHome = () => {
    navigate('/');
  };

  const handleLogin = () => {
    navigate('/login');
  };

  return (
    <div className='toolbar'>
      <div className='toolbar-logo-container'>
        <img src={logo} alt="Carzilla Logo" className='toolbar-logo' />
        <span className='toolbar-title'>Carzilla - Find Your Dream Car</span>
      </div>
      <div className='toolbar-buttons'>
        <button className='toolbar-button' onClick={handleHome}>Home</button>
        <button className='toolbar-button' onClick={handleLogin}>Login</button>
        <button className='toolbar-button'>Settings</button>
      </div>
    </div>
  );
};

export default ToolBar;