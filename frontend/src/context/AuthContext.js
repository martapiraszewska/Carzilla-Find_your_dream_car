import React, { createContext, useState, useContext } from 'react';

// This is used to provide global state whether the user is logged in or not
const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [isLogged, setIsLogged] = useState(false);

  const login = () => setIsLogged(true);
  const logout = () => setIsLogged(false);

  return (
    <AuthContext.Provider value={{ isLogged, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);