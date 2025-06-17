import React, { useState, useEffect } from 'react';
import './AddForm.css';
import ToolBar from '../elements/ToolBar';

const AddEmployee = () => {
  const [formData, setFormData] = useState({
    Name: '',
    Surname: '',
    Gender: '',
    Salary: '',
    Date_of_birth: '',
    Phone_number: '',
    Employee_status_ID: '',
    Car_dealer_ID: '',
    Position_ID: ''
  });
  const [dealers, setDealers] = useState([]);
  const [statuses, setStatuses] = useState([]);
  const [positions, setPositions] = useState([]);
  const [message, setMessage] = useState('');
  const [messageType, setMessageType] = useState(''); // 'success' or 'error'

  // Fetch car dealers for dropdown
  useEffect(() => {
    fetch('/car_dealers/')
      .then((res) => res.json())
      .then((data) => setDealers(data))
      .catch(() => setDealers([]));
  }, []);

  // Fetch employee statuses for dropdown
  useEffect(() => {
    fetch('/employee_status/')
      .then((res) => res.json())
      .then((data) => setStatuses(data))
      .catch(() => setStatuses([]));
  }, []);

  // Fetch positions for dropdown
  useEffect(() => {
    fetch('/positions/')
      .then((res) => res.json())
      .then((data) => setPositions(data))
      .catch(() => setPositions([]));
  }, []);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setMessage('');
    setMessageType('');
    fetch('/employees/add', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(formData),
    })
      .then(async (response) => {
        const data = await response.json();
        if (response.ok) {
          setMessage(data.message || 'Employee added successfully!');
          setMessageType('success');
          setFormData({
            Name: '',
            Surname: '',
            Gender: '',
            Salary: '',
            Date_of_birth: '',
            Phone_number: '',
            Employee_status_ID: '',
            Car_dealer_ID: '',
            Position_ID: ''
          });
        } else {
          setMessage(data.error || 'Failed to add employee.');
          setMessageType('error');
        }
      })
      .catch(() => {
        setMessage('Error adding employee.');
        setMessageType('error');
      });
  };

  return (
    <div className="hire-page">
      <ToolBar />
      <h1 className="hire-title">Hire a New Employee</h1>
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
          type="number"
          name="Salary"
          placeholder="Salary"
          value={formData.Salary}
          onChange={handleChange}
        />
        <input
          type="date"
          name="Date_of_birth"
          placeholder="Date of Birth"
          value={formData.Date_of_birth}
          onChange={handleChange}
          required
        />
        <input
          type="text"
          name="Phone_number"
          placeholder="Phone Number"
          value={formData.Phone_number}
          onChange={handleChange}
        />
        <select
          name="Employee_status_ID"
          value={formData.Employee_status_ID}
          onChange={handleChange}
          required
        >
          <option value="">Employee Status</option>
          {statuses.map((status) => (
            <option key={status.Employee_status_ID} value={status.Employee_status_ID}>
              {status.Status_name}
            </option>
          ))}
        </select>
        <select
          name="Car_dealer_ID"
          value={formData.Car_dealer_ID}
          onChange={handleChange}
          required
        >
          <option value="">Car Dealer</option>
          {dealers.map((dealer) => (
            <option key={dealer.Car_dealer_ID} value={dealer.Car_dealer_ID}>
              {dealer.Name}
            </option>
          ))}
        </select>
        <select
          name="Position_ID"
          value={formData.Position_ID}
          onChange={handleChange}
          required
        >
          <option value="">Position</option>
          {positions.map((pos) => (
            <option key={pos.Position_ID} value={pos.Position_ID}>
              {pos.Position_name}
            </option>
          ))}
        </select>
        <button type="submit" className="hire-button">
          Hire Employee
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

export default AddEmployee;