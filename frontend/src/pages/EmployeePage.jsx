import React, { useState, useEffect } from 'react';
import './EmployeePage.css';
import { useNavigate } from 'react-router-dom';
import ToolBar from '../elements/ToolBar';

const EmployeePage = () => {
  const [employees, setEmployees] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    fetch('/employees')
      .then((response) => response.json())
      .then((data) => setEmployees(data))
      .catch((error) => console.error('Error fetching employees:', error));
  }, []);

  const handleHire = () => {
    navigate('/hire');
  };

   const handleFire = () => {
    alert("Fired");
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