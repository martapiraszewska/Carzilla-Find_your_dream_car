import React, { useState } from 'react';
import './AddForm.css';
import ToolBar from '../elements/ToolBar';

const AddClient = () => {
  const [formData, setFormData] = useState({
    Name: '',
    Surname: '',
    Gender: '',
    Mail: '',
    Phone: '',
    City: '',
  });
  const [message, setMessage] = useState('');
  const [messageType, setMessageType] = useState(''); // 'success' or 'error'

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setMessage('');
    setMessageType('');

    // Prepare payload
    const payload = {
      Name: formData.Name,
      Surname: formData.Surname,
      Gender: formData.Gender,
      Mail: formData.Mail,
      Phone: formData.Phone,
      City: formData.City,
    };

    fetch('/clients/add', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    })
      .then(async (response) => {
        const data = await response.json();
        if (response.ok) {
          setMessage(data.message || 'Client added successfully!');
          setMessageType('success');
          setFormData({
            Name: '',
            Surname: '',
            Gender: '',
            Mail: '',
            Phone: '',
            City: '',
          });
        } else {
          setMessage(data.error || 'Failed to add client.');
          setMessageType('error');
        }
      })
      .catch(() => {
        setMessage('Error adding client.');
        setMessageType('error');
      });
  };

  return (
    <div className="hire-page">
      <ToolBar />
      <h1 className="hire-title">Add New Client</h1>
      <form className="hire-form" onSubmit={handleSubmit}>
        <input
          type="text"
          name="Name"
          placeholder="Name"
          value={formData.Name}
          onChange={handleChange}
          required
        />
        <input
          type="text"
          name="Surname"
          placeholder="Surname"
          value={formData.Surname}
          onChange={handleChange}
          required
        />
        <select
          name="Gender"
          value={formData.Gender}
          onChange={handleChange}
          required
        >
          <option value="">Gender</option>
          <option value="M">Male</option>
          <option value="F">Female</option>
          <option value="O">Other</option>
        </select>
        <input
          type="email"
          name="Mail"
          placeholder="Email"
          value={formData.Mail}
          onChange={handleChange}
          required
        />
        <input
          type="text"
          name="Phone"
          placeholder="Phone"
          value={formData.Phone}
          onChange={handleChange}
          required
        />
        <input
          type="text"
          name="City"
          placeholder="City"
          value={formData.City}
          onChange={handleChange}
          required
        />
        <button type="submit" className="hire-button">
          Add Client
        </button>
      </form>
      {message && (
        <div className={`addcar-message ${messageType}`}>
          {message}
        </div>
      )}
    </div>
  );
};

export default AddClient;