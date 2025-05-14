import React, { useState } from 'react';
import './AddForm.css';
import ToolBar from '../elements/ToolBar';

const AddCar = () => {
  const [formData, setFormData] = useState({
    brand: '',
    model: '',
    year: '',
    price: '',
    color: '',
    mileage: '',
    condition_id: '',
    dealer_id: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch('/cars', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(formData),
    })
      .then((response) => response.json())
      .then((data) => {
        alert(data.message || 'Car added successfully!');
        setFormData({
          brand: '',
          model: '',
          year: '',
          price: '',
          color: '',
          mileage: '',
          condition_id: '',
          dealer_id: '',
        });
      })
      .catch((error) => console.error('Error adding car:', error));
  };

  return (
    <div className="hire-page">
      <ToolBar />
      <h1 className="hire-title">Add a New Car</h1>
      <form className="hire-form" onSubmit={handleSubmit}>
        <input
          type="text"
          name="brand"
          placeholder="Brand"
          value={formData.brand}
          onChange={handleChange}
          required
        />
        <input
          type="text"
          name="model"
          placeholder="Model"
          value={formData.model}
          onChange={handleChange}
          required
        />
        <input
          type="number"
          name="year"
          placeholder="Year"
          value={formData.year}
          onChange={handleChange}
          required
        />
        <input
          type="number"
          name="price"
          placeholder="Price"
          value={formData.price}
          onChange={handleChange}
          required
        />
        <input
          type="text"
          name="color"
          placeholder="Color"
          value={formData.color}
          onChange={handleChange}
        />
        <input
          type="number"
          name="mileage"
          placeholder="Mileage"
          value={formData.mileage}
          onChange={handleChange}
        />
        <input
          type="number"
          name="condition_id"
          placeholder="Condition ID"
          value={formData.condition_id}
          onChange={handleChange}
          required
        />
        <input
          type="number"
          name="dealer_id"
          placeholder="Dealer ID"
          value={formData.dealer_id}
          onChange={handleChange}
          required
        />
        <button type="submit" className="hire-button">
          Add Car
        </button>
      </form>
    </div>
  );
};

export default AddCar;