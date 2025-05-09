import React from 'react';
import './LoginPage.css'
import ToolBar from '../elements/ToolBar.js';
import SearchBar from '../elements/SearchBar.js';

const LoginPage = () => {
  return (
    <div className='loginpage'>
      <ToolBar></ToolBar>
      <div className='login-box'>
        <input type='text' className='credentials-input' placeholder='Wpisz login...'></input>
        <input type='text' className='credentials-input' placeholder='Wpisz hasło...'></input>
      </div>
    </div>
  );
}

export default LoginPage;