import React, { useState } from 'react';
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
    Login_credentials_ID: '',
    Position_ID: ''
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch('/employees/add', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(formData),
    })
      .then((response) => response.json())
      .then((data) => {
        alert(data.message || 'Employee added successfully!');
        // setFormData({
        //   Name: '',
        //   Surname: '',
        //   Gender: '',
        //   Salary: '',
        //   Date_of_birth: '',
        //   Phone_number: '',
        //   Employee_status_id: '',
        //   Car_dealer_id: '',
        //   Login_credentials_id: '',
        // });
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
        <input
          type="text"
          name="Gender"
          placeholder="Gender"
          value={formData.Gender}
          onChange={handleChange}
          required
        />
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
        <input
          type="number"
          name="Employee_status_ID"
          placeholder="Employee Status ID"
          value={formData.Employee_status_ID}
          onChange={handleChange}
          required
        />
        <input
          type="number"
          name="Car_dealer_ID"
          placeholder="Car Dealer ID"
          value={formData.Car_dealer_ID}
          onChange={handleChange}
          required
        />
        <input
          type="number"
          name="Login_credentials_ID"
          placeholder="Login Credentials ID"
          value={formData.Login_credentials_ID}
          onChange={handleChange}
          required
        />
        <input
          type="number"
          name="Position_ID"
          placeholder="Position ID"
          value={formData.Position_ID}
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