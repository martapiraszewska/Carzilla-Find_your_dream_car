import React, { useState, useEffect } from 'react';
import './EmployeePage.css';
import { useNavigate } from 'react-router-dom';
import ToolBar from '../elements/ToolBar';

const EmployeePage = () => {
  // Mocked employee data
  const [employees, setEmployees] = useState([
  // { id: 1, name: 'John Doe', position: 'Sales Manager' },
  // { id: 2, name: 'Jane Smith', position: 'Accountant' },
  // { id: 3, name: 'Alice Johnson', position: 'HR Specialist' },
  // { id: 4, name: 'Bob Brown', position: 'Mechanic' },
  ]);
  const navigate = useNavigate();

  const handleFetchEmployees = () => {
    const options = {
        method: 'GET',
        headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Headers': 'Origin, X-Requested-With, Content-Type, Accept', 'credentials': 'include'},
    };
    fetch('/employees/search', options).then((response) => {
      if (response.status === 200) {
          response.json().then(data => {
            setEmployees(data);
            console.log(data);
            return data;
          })
      }
      else{
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
    fetch(`/employees/remove/${id}`, {
      method: 'DELETE',
      headers: { 'Content-Type': 'application/json' },
    })
      .then((response) => response.json())
      .then((data) => {
        alert(data.message || 'Employee fired successfully!');
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
      .catch((error) => console.error('Error firing employee:', error));
  };

  return (
    <div className="employee-page">
      <ToolBar />
      <h1 className="employee-title">Employee Management</h1>
      <ul className="employee-list">
        {employees.map((employee) => (
          <li key={employee.Employee_ID} className="employee-item">
            <span className="employee-name">{employee.Name}</span>
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
      <button className="hire-button" onClick={handleHire}>
        Hire
      </button>
    </div>
  );
};

export default EmployeePage;