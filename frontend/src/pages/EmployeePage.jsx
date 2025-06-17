import React, { useState, useEffect } from 'react';
import './EmployeePage.css';
import { useNavigate } from 'react-router-dom';
import ToolBar from '../elements/ToolBar';

const EmployeePage = () => {
  const [employees, setEmployees] = useState([]);
  const [message, setMessage] = useState('');
  const [messageType, setMessageType] = useState(''); // 'success' or 'error'
  const navigate = useNavigate();

  const handleFetchEmployees = () => {
    const options = {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Origin, X-Requested-With, Content-Type, Accept',
        'credentials': 'include'
      },
    };
    fetch('/employees/search', options).then((response) => {
      if (response.status === 200) {
        response.json().then(data => {
          setEmployees(data);
          return data;
        });
      } else {
        console.log("unable to fetch profile data", response);
      }
    });
  };

  useEffect(() => {
    handleFetchEmployees();
  }, []);

  const handleHire = () => {
    navigate('/hire');
  };

  const handleFire = (id) => {
    setMessage('');
    setMessageType('');
    fetch(`/employees/remove/${id}`, {
      method: 'DELETE',
      headers: { 'Content-Type': 'application/json' },
    })
      .then((response) => response.json())
      .then((data) => {
        setMessage(data.message || 'Employee fired successfully!');
        setMessageType('success');
        // Remove fired employee from list
        setEmployees((prev) => prev.filter(emp => emp.Employee_ID !== id));
      })
      .catch(() => {
        setMessage('Error firing employee.');
        setMessageType('error');
      });
  };

  return (
    <div className="employee-page">
      <ToolBar />
      <h1 className="employee-title">Employee Management</h1>
      <button className="hire-button" onClick={handleHire}>
        Hire
      </button>
      {message && (
        <div className={`employee-message ${messageType}`}>
          {message}
        </div>
      )}
      <ul className="employee-list">
        {employees.map((employee) => (
          <li key={employee.Employee_ID} className="employee-item">
            <span className="employee-name">
              {employee.Name} {employee.Surname}
            </span>
            <span className="employee-position">{employee.Position_name}</span>
            <button
              className="fire-button"
              onClick={() => handleFire(employee.Employee_ID)}
            >
              Fire
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default EmployeePage;