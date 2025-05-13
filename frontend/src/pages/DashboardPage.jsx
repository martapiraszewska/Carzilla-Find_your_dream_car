import React from 'react';
import './DashboardPage.css';
import ToolBar from '../elements/ToolBar.jsx';
import { useNavigate } from 'react-router-dom';

const DashboardPage = () => {
  const navigate = useNavigate();

  const handleNavigation = (path) => {
    navigate(path);
  };

  return (
    <div className="dashboard-page">
      <ToolBar />
      <div className="dashboard-tiles">
        <div className="tile" onClick={() => handleNavigation('/cars')}>
          <h2>Cars</h2>
        </div>
        <div className="tile" onClick={() => handleNavigation('/employees')}>
          <h2>Employees</h2>
        </div>
        <div className="tile" onClick={() => handleNavigation('/invoices')}>
          <h2>Invoices</h2>
        </div>
        <div className="tile" onClick={() => handleNavigation('/clients')}>
          <h2>Clients</h2>
        </div>
        <div className="tile" onClick={() => handleNavigation('/stats')}>
          <h2>Stats</h2>
        </div>
      </div>
    </div>
  );
};

export default DashboardPage;