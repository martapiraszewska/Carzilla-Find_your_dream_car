import React, { useState } from 'react';
import './AddForm.css';
import ToolBar from '../elements/ToolBar';

const AddEmployee = () => {
  const [formData, setFormData] = useState({
    name: '',
    surname: '',
    gender: '',
    salary: '',
    date_of_birth: '',
    phone_number: '',
    employee_status_id: '',
    car_dealer_id: '',
    login_credentials_id: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch('/employees', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(formData),
    })
      .then((response) => response.json())
      .then((data) => {
        alert(data.message || 'Employee added successfully!');
        setFormData({
          name: '',
          surname: '',
          gender: '',
          salary: '',
          date_of_birth: '',
          phone_number: '',
          employee_status_id: '',
          car_dealer_id: '',
          login_credentials_id: '',
        });
      })
      .catch((error) => console.error('Error adding employee:', error));
  };

  return (
    <div className="hire-page">
        <ToolBar />
      <h1 className="hire-title">Hire a New Employee</h1>
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
          type="text"
          name="gender"
          placeholder="Gender"
          value={formData.gender}
          onChange={handleChange}
          required
        />
        <input
          type="number"
          name="salary"
          placeholder="Salary"
          value={formData.salary}
          onChange={handleChange}
        />
        <input
          type="date"
          name="date_of_birth"
          placeholder="Date of Birth"
          value={formData.date_of_birth}
          onChange={handleChange}
          required
        />
        <input
          type="text"
          name="phone_number"
          placeholder="Phone Number"
          value={formData.phone_number}
          onChange={handleChange}
        />
        <input
          type="number"
          name="employee_status_id"
          placeholder="Employee Status ID"
          value={formData.employee_status_id}
          onChange={handleChange}
          required
        />
        <input
          type="number"
          name="car_dealer_id"
          placeholder="Car Dealer ID"
          value={formData.car_dealer_id}
          onChange={handleChange}
          required
        />
        <input
          type="number"
          name="login_credentials_id"
          placeholder="Login Credentials ID"
          value={formData.login_credentials_id}
          onChange={handleChange}
          required
        />
        <button type="submit" className="hire-button">
          Hire Employee
        </button>
      </form>
    </div>
  );
};

export default AddEmployee;