import React, { useState } from 'react';
import './AddForm.css';
import ToolBar from '../elements/ToolBar';

const AddClient = () => {
  const [formData, setFormData] = useState({
    name: '',
    surname: '',
    email: '',
    phone: '',
    address: '',
    city: '',
    date_of_birth: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch('/clients', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(formData),
    })
      .then((response) => response.json())
      .then((data) => {
        alert(data.message || 'Client added successfully!');
        setFormData({
          name: '',
          surname: '',
          email: '',
          phone: '',
          address: '',
          city: '',
          date_of_birth: '',
        });
      })
      .catch((error) => console.error('Error adding client:', error));
  };

  return (
    <div className="hire-page">
      <ToolBar />
      <h1 className="hire-title">Add New Client</h1>
      <form className="hire-form" onSubmit={handleSubmit}>
        <input
          type="text"
          name="name"
          placeholder="Name"
          value={formData.name}
          onChange={handleChange}
          required
        />
        <input
          type="text"
          name="surname"
          placeholder="Surname"
          value={formData.surname}
          onChange={handleChange}
          required
        />
        <input
          type="email"
          name="email"
          placeholder="Email"
          value={formData.email}
          onChange={handleChange}
          required
        />
        <input
          type="text"
          name="phone"
          placeholder="Phone"
          value={formData.phone}
          onChange={handleChange}
        />
        <input
          type="text"
          name="address"
          placeholder="Address"
          value={formData.address}
          onChange={handleChange}
        />
        <input
          type="text"
          name="city"
          placeholder="City"
          value={formData.city}
          onChange={handleChange}
        />
        <input
          type="date"
          name="date_of_birth"
          placeholder="Date of Birth"
          value={formData.date_of_birth}
          onChange={handleChange}
        />
        <button type="submit" className="hire-button">
          Add Client
        </button>
      </form>
    </div>
  );
};

export default AddClient;