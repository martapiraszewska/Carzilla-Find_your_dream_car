import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import './ProfilePage.css';

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


  const handleLogout = () => {
    logout(); // Set the global login state to false
    navigate('/'); // Redirect to the homepage
  };

  return (
    <div className="profile-page">
      <h1 className="profile-title">Profile</h1>
      <div className="profile-stats">
        <h2>Account Stats</h2>
        <ul>
          <li>Cars Sold: 25</li>
          <li>Total Profit: $50,000</li>
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