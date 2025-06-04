import React from 'react';
import ToolBar from '../elements/ToolBar';
import './StatsPage.css';
import crownIcon from '../assets/crown.png';

const StatsPage = () => {
  // Mocked stats data
  const employeeOfMonth = {
    name: 'Alice Johnson',
    position: 'HR Specialist',
  };

  const stats = {
    carsSold: 37,
    profit: 125000,
    bestMonth: 'April 2024',
    avgDealValue: 3378,
  };

  return (
    <div className="stats-page">
      <ToolBar />
      <h1 className="stats-title">Company Stats</h1>
      <div className="stats-employee-month">
        <h2>Employee of the Month</h2>
        <img src={crownIcon} alt="Employee of the Month" className="employee-crown" />
        <div className="employee-name">{employeeOfMonth.name}</div>
        <div className="employee-position">{employeeOfMonth.position}</div>
      </div>
      <div className="stats-boxes">
        <div className="stat-box">
          <span className="stat-label">Cars Sold</span>
          <span className="stat-value">{stats.carsSold}</span>
        </div>
        <div className="stat-box">
          <span className="stat-label">Total Profit</span>
          <span className="stat-value">${stats.profit.toLocaleString()}</span>
        </div>
        <div className="stat-box">
          <span className="stat-label">Best Month</span>
          <span className="stat-value">{stats.bestMonth}</span>
        </div>
        <div className="stat-box">
          <span className="stat-label">Avg. Deal Value</span>
          <span className="stat-value">${stats.avgDealValue}</span>
        </div>
      </div>
    </div>
  );
};

export default StatsPage;