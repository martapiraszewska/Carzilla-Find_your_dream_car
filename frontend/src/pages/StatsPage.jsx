import React, { useState, useEffect } from 'react';
import ToolBar from '../elements/ToolBar';
import './StatsPage.css';
import crownIcon from '../assets/crown.png';

const StatsPage = () => {
  // Employee of the Month state
  const [employeeOfMonth, setEmployeeOfMonth] = useState(null);
  const [eomLoading, setEomLoading] = useState(true);
  const [eomMessage, setEomMessage] = useState('');

  // Bonus stats state
  const [stats, setStats] = useState(null);
  const [statsLoading, setStatsLoading] = useState(true);
  const [statsMessage, setStatsMessage] = useState('');

  // Fetch Employee of the Month
  useEffect(() => {
    setEomLoading(true);
    setEomMessage('');
    fetch('/stats/employee_of_month/search')
      .then((response) => {
        if (response.status === 200) {
          return response.json();
        } else if (response.status === 204) {
          setEomMessage('No data for current time period.');
          setEmployeeOfMonth(null);
          setEomLoading(false);
          return null;
        } else {
          throw new Error('Unable to fetch employee of the month');
        }
      })
      .then((data) => {
        if (data) {
          setEmployeeOfMonth(data);
        }
        setEomLoading(false);
      })
      .catch(() => {
        setEomMessage('Error loading employee of the month.');
        setEmployeeOfMonth(null);
        setEomLoading(false);
      });
  }, []);

  // Fetch bonus stats from /profile/search
  useEffect(() => {
    setStatsLoading(true);
    setStatsMessage('');
    fetch('/profile/search', {
      method: 'GET',
      headers: { 'Content-Type': 'application/json' },
      credentials: 'include',
    })
      .then((response) => {
        if (response.status === 200) {
          return response.json();
        } else if (response.status === 204) {
          setStatsMessage('No stats data for current user.');
          setStats(null);
          setStatsLoading(false);
          return null;
        } else {
          throw new Error('Unable to fetch stats');
        }
      })
      .then((data) => {
        if (data) {
          setStats(data);
        }
        setStatsLoading(false);
      })
      .catch(() => {
        setStatsMessage('Error loading stats.');
        setStats(null);
        setStatsLoading(false);
      });
  }, []);

  return (
    <div className="stats-page">
      <ToolBar />
      <h1 className="stats-title">Company Stats</h1>
      <div className="stats-employee-month">
        <h2>Employee of the Month</h2>
        <img src={crownIcon} alt="Employee of the Month" className="employee-crown" />
        {eomLoading && <div>Loading...</div>}
        {eomMessage && <div className="stats-message">{eomMessage}</div>}
        {employeeOfMonth && (
          <>
            <div className="employee-name">
              {employeeOfMonth.Name} {employeeOfMonth.Surname}
            </div>
            <div className="employee-position">{employeeOfMonth.Position}</div>
            <div className="employee-sales">Sales: {employeeOfMonth.Sales}</div>
          </>
        )}
      </div>
      <h2 className="stats-title">Your Bonus Stats</h2>
      {statsLoading && <div>Loading...</div>}
      {statsMessage && <div className="stats-message">{statsMessage}</div>}
      {stats && (
        <div className="stats-boxes">
          <div className="stat-box">
            <span className="stat-label">Cars Sold</span>
            <span className="stat-value">{stats.carsSold}</span>
          </div>
          <div className="stat-box">
            <span className="stat-label">Total Profit</span>
            <span className="stat-value">
              ${stats.profit ? stats.profit.toLocaleString() : 0}
            </span>
          </div>
        </div>
      )}
    </div>
  );
};

export default StatsPage;