import React, { useState } from 'react';
import './EmployeePage.css';
import { useNavigate } from 'react-router-dom';
import ToolBar from '../elements/ToolBar';

const EmployeePage = () => {
  // Mocked employee data
  const [employees, setEmployees] = useState([
    { id: 1, name: 'John Doe', position: 'Sales Manager' },
    { id: 2, name: 'Jane Smith', position: 'Accountant' },
    { id: 3, name: 'Alice Johnson', position: 'HR Specialist' },
    { id: 4, name: 'Bob Brown', position: 'Mechanic' },
  ]);
  const navigate = useNavigate();

  const handleHire = () => {
    navigate('/hire');
  };

  const handleFire = (id) => {
    setEmployees((prev) => prev.filter((employee) => employee.id !== id));
  };

  return (
    <div className="employee-page">
      <ToolBar />
      <h1 className="employee-title">Employee Management</h1>
      <ul className="employee-list">
        {employees.map((employee) => (
          <li key={employee.id} className="employee-item">
            <span className="employee-name">{employee.name}</span>
            <span className="employee-position">{employee.position}</span>
            <button
              className="fire-button"
              onClick={() => handleFire(employee.id)}
            >
              Fire
            </button>
          </li>
        ))}
      </ul>
      <button className="hire-button" onClick={handleHire}>
        Hire
      </button>
    </div>
  );
};

export default EmployeePage;