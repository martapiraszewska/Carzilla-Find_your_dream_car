import React, { useState } from 'react';
import './AddForm.css';
import ToolBar from '../elements/ToolBar';

const AddCar = () => {
  const [formData, setFormData] = useState({
    Brand: '',
    Model: '',
    Color: '',
    Mileage: '',
    Price: '',
    Car_condition_ID: '',
    Car_dealer_ID: '',
  });
  const [dealers, setDealers] = useState([]);
  const [dealersLoaded, setDealersLoaded] = useState(false);
  const [conditions, setConditions] = useState([]);
  const [conditionsLoaded, setConditionsLoaded] = useState(false);
  const [message, setMessage] = useState('');
  const [messageType, setMessageType] = useState(''); // 'success' or 'error'

  const fetchDealers = () => {
    if (dealersLoaded) return;
    fetch('/car_dealers/')
      .then((res) => res.json())
      .then((data) => {
        setDealers(data);
        setDealersLoaded(true);
      })
      .catch(() => {
        setDealers([]);
        setDealersLoaded(true);
      });
  };

  const fetchConditions = () => {
    if (conditionsLoaded) return;
    fetch('/car_conditions/')
      .then((res) => res.json())
      .then((data) => {
        setConditions(data);
        setConditionsLoaded(true);
      })
      .catch(() => {
        setConditions([]);
        setConditionsLoaded(true);
      });
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleDealerFocus = () => {
    fetchDealers();
  };

  const handleConditionFocus = () => {
    fetchConditions();
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setMessage('');
    setMessageType('');

    // Ensure IDs are sent as strings of digits
    const payload = {
      ...formData,
      Car_condition_ID: String(formData.Car_condition_ID),
      Car_dealer_ID: String(formData.Car_dealer_ID),
    };

    // Validate IDs are not empty and are digits
    if (
      !payload.Car_condition_ID ||
      !/^\d+$/.test(payload.Car_condition_ID) ||
      !payload.Car_dealer_ID ||
      !/^\d+$/.test(payload.Car_dealer_ID)
    ) {
      setMessage('Please select both a valid condition and dealer.');
      setMessageType('error');
      return;
    }

    fetch('/cars/add', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    })
      .then(async (response) => {
        const data = await response.json();
        if (response.ok) {
          setMessage(data.message || 'Car added successfully!');
          setMessageType('success');
          setFormData({
            Brand: '',
            Model: '',
            Color: '',
            Mileage: '',
            Price: '',
            Car_condition_ID: '',
            Car_dealer_ID: '',
          });
          setDealersLoaded(false);
          setConditionsLoaded(false);
        } else {
          setMessage(data.error || 'Failed to add car.');
          setMessageType('error');
        }
      })
      .catch((error) => {
        setMessage('Error adding car.');
        setMessageType('error');
        console.error('Error adding car:', error);
      });
  };

  return (
    <div className="hire-page">
      <ToolBar />
      <h1 className="hire-title">Add a New Car</h1>
      <form className="hire-form" onSubmit={handleSubmit}>
        <input
          type="text"
          name="Brand"
          placeholder="Brand"
          value={formData.Brand}
          onChange={handleChange}
          required
        />
        <input
          type="text"
          name="Model"
          placeholder="Model"
          value={formData.Model}
          onChange={handleChange}
          required
        />
        <input
          type="text"
          name="Color"
          placeholder="Color"
          value={formData.Color}
          onChange={handleChange}
          required
        />
        <input
          type="number"
          name="Mileage"
          placeholder="Mileage"
          value={formData.Mileage}
          onChange={handleChange}
          min="0"
          required
        />
        <input
          type="number"
          name="Price"
          placeholder="Price"
          value={formData.Price}
          onChange={handleChange}
          min="0"
          required
        />
        <select
          name="Car_condition_ID"
          value={formData.Car_condition_ID}
          onChange={handleChange}
          onFocus={handleConditionFocus}
          required
        >
          <option value="">Condition</option>
          {conditions.map((condition) => (
            <option key={condition.Car_condition_ID} value={condition.Car_condition_ID}>
              {condition.Condition}
            </option>
          ))}
        </select>
        <select
          name="Car_dealer_ID"
          value={formData.Car_dealer_ID}
          onChange={handleChange}
          onFocus={handleDealerFocus}
          required
        >
          <option value="">Dealer</option>
          {dealers.map((dealer) => (
            <option key={dealer.Car_dealer_ID} value={dealer.Car_dealer_ID}>
              {dealer.Name}
            </option>
          ))}
        </select>
        <button type="submit" className="hire-button">
          Add Car
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

export default AddCar;