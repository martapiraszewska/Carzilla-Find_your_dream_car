import React from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import './ProfilePage.css';

const ProfilePage = () => {
  const { logout } = useAuth(); // Access the logout function
  const navigate = useNavigate();

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