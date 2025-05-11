import React from 'react';
import './HomePage.css';
import ToolBar from '../elements/ToolBar.js';
import SearchBar from '../elements/SearchBar.js';
import DashboardPage from './DashboardPage.js';
import { useAuth } from '../context/AuthContext';

const HomePage = () => {
  const { isLogged } = useAuth(); // Access the global login state

  return (
    <div className="homepage">
      <ToolBar />
      <div>
        {isLogged ? <DashboardPage /> : <SearchBar />}
      </div>
    </div>
  );
};

export default HomePage;