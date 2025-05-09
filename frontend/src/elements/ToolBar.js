import React from 'react';
import { useNavigate } from 'react-router-dom';
import './ToolBar.css';

const ToolBar = () => {
  const navigate = useNavigate();
  
  const handleHome = () => {
    navigate('/');
  }
  
  const handleLogin = () => {
    navigate('/login');
  };

  return (
    <div className='toolbar'>
      <button className='toolbar-button' onClick={handleHome}>Home</button>
      <button className='toolbar-button' onClick={handleLogin}>Login</button>
      <button className='toolbar-button'>Settings</button>
    </div>
  );
};

export default ToolBar;