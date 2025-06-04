import React, { useState } from 'react';
import './AddForm.css';
import ToolBar from '../elements/ToolBar';

const AddInvoice = () => {
  const [formData, setFormData] = useState({
    car: '',
    employee: '',
    client: '',
    amount: '',
    date: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e) => {
    // for now only
    e.preventDefault();
    fetch('/invoices', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(formData),
    })
      .then((response) => response.json())
      .then((data) => {
        alert(data.message || 'Invoice added successfully!');
        setFormData({
          car: '',
          employee: '',
          client: '',
          amount: '',
          date: '',
        });
      })
      .catch((error) => console.error('Error adding invoice:', error));
  };

  return (
    <div className="hire-page">
      <ToolBar />
      <h1 className="hire-title">Invoice</h1>
      <form className="hire-form" onSubmit={handleSubmit}>
        <input
          type="text"
          name="car"
          placeholder="Car (e.g. Toyota Corolla)"
          value={formData.car}
          onChange={handleChange}
          required
        />
        <input
          type="text"
          name="employee"
          placeholder="Employee (e.g. John Doe)"
          value={formData.employee}
          onChange={handleChange}
          required
        />
        <input
          type="text"
          name="client"
          placeholder="Client (e.g. Jane Smith)"
          value={formData.client}
          onChange={handleChange}
          required
        />
        <input
          type="number"
          name="amount"
          placeholder="Amount"
          value={formData.amount}
          onChange={handleChange}
          required
        />
        <input
          type="date"
          name="date"
          placeholder="Date"
          value={formData.date}
          onChange={handleChange}
          required
        />
        <button type="submit" className="hire-button">
          Submit
        </button>
      </form>
    </div>
  );
};

export default AddInvoice;