import React, { useState, useEffect } from 'react';
import './AddForm.css';
import ToolBar from '../elements/ToolBar';

const AddInvoice = () => {
  const [formData, setFormData] = useState({
    employee: '',
    client: '',
    amount: '',
    nip: '',
  });
  const [employees, setEmployees] = useState([]);
  const [clients, setClients] = useState([]);
  const [message, setMessage] = useState('');
  const [messageType, setMessageType] = useState(''); // 'success' or 'error'

  // Fetch employees for dropdown
  useEffect(() => {
    fetch('/employees/search')
      .then((res) => res.json())
      .then((data) => setEmployees(data))
      .catch(() => setEmployees([]));
  }, []);

  // Fetch clients for dropdown
  useEffect(() => {
    fetch('/clients/search')
      .then((res) => res.json())
      .then((data) => setClients(data))
      .catch(() => setClients([]));
  }, []);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setMessage('');
    setMessageType('');
    fetch('/invoices/add', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(formData),
    })
      .then(async (response) => {
        const data = await response.json();
        if (response.ok) {
          setMessage(data.message || 'Invoice added successfully!');
          setMessageType('success');
          setFormData({
            employee: '',
            client: '',
            amount: '',
            nip: '',
          });
        } else {
          setMessage(data.error || 'Failed to add invoice.');
          setMessageType('error');
        }
      })
      .catch(() => {
        setMessage('Error adding invoice.');
        setMessageType('error');
      });
  };

  return (
    <div className="hire-page">
      <ToolBar />
      <h1 className="hire-title">Add Invoice</h1>
      <form className="hire-form" onSubmit={handleSubmit}>
        <select
          name="employee"
          value={formData.employee}
          onChange={handleChange}
          required
        >
          <option value="">Select Employee</option>
          {employees.map((emp) => (
            <option key={emp.Employee_ID} value={emp.Employee_ID}>
              {emp.Name} {emp.Surname}
            </option>
          ))}
        </select>
        <select
          name="client"
          value={formData.client}
          onChange={handleChange}
          required
        >
          <option value="">Select Client</option>
          {clients.map((client) => (
            <option key={client.Client_ID} value={client.Client_ID}>
              {client.Name} {client.Surname}
            </option>
          ))}
        </select>
        <input
          type="number"
          name="amount"
          placeholder="Amount"
          value={formData.amount}
          onChange={handleChange}
          required
        />
        <input
          type="text"
          name="nip"
          placeholder="NIP"
          value={formData.nip}
          onChange={handleChange}
          required
        />
        <button type="submit" className="hire-button">
          Submit
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

export default AddInvoice;