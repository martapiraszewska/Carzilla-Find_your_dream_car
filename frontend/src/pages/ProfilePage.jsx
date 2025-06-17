import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import './ProfilePage.css';
import ToolBar from '../elements/ToolBar';

const ProfilePage = () => {
  const { logout } = useAuth(); // Access the logout function
  const navigate = useNavigate();

  const [stats, setStats] = useState([]);
  const handleGetData = () => {
    const options = {
        method: 'GET',
        headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Headers': 'Origin, X-Requested-With, Content-Type, Accept', 'credentials': 'include'},
    };
    fetch('/profile/search', options).then((response) => {
      if (response.status === 200) {
          response.json().then(data => {
            setStats(data);
            console.log(data);
            return data;
          })
      }
      else{
          console.log("unable to fetch profile data", response);
      }
    });
  };

  useEffect(() => {
      handleGetData();
    }, []);


  const handleLogout = () => {
    fetch('/auth/logout', {
      method: 'POST',
    })
    .then(response => {
      if (response.ok) {
        logout();
      } else {
        alert('Something went wrong. Please try again.');
      }
    })
  };


  return (
    <div className="profile-page">
      <ToolBar />
      <h1 className="profile-title">Profile</h1>
      <div className="profile-stats">
        <h2>Account Stats</h2>
        <ul>
          <li>Number of Car Dealers: {stats.carDealersAmount}</li>
          <li>Cars Sold: {stats.carsSold}</li>
          <li>Total Profit: ${stats.profit}</li>
          <li>Active Since: January 2023</li>
        </ul>
      </div>
      <button className="logout-button" onClick={handleLogout}>
        Logout
      </button>
    </div>
  );
};

export default ProfilePage;