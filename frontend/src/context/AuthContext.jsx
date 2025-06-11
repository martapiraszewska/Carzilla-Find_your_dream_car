import React, { createContext, useState, useContext, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

// This is used to provide global state whether the user is logged in or not
const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [isLogged, setIsLogged] = useState(false);

  const login = () => {setIsLogged(true); navigate('/dashboard');};  
  const logout = () => {setIsLogged(false); navigate('/')};
  const navigate = useNavigate();
  
  useEffect(() => {
    fetch('/auth/status', {
      method: 'GET',
    })
    .then(res => res.json())
    .then(data => {
      if (data.authenticated){
        login();
      }
    })
    .catch(err => {
      console.error('Auth check failed:', err);
    });
  }, []);

  return (
    <AuthContext.Provider value={{ isLogged, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);