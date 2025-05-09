import React from 'react';
import './HomePage.css'
import ToolBar from '../elements/ToolBar.js';
import SearchBar from '../elements/SearchBar.js';

const HomePage = () => {
  return (
    <div className="homepage">
      <div>
        <ToolBar></ToolBar>
      </div>
    </div>
  );
}

export default HomePage;