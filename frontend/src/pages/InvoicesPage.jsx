import React, { useState } from 'react';
import ToolBar from '../elements/ToolBar';
import './InvoicesPage.css';
import { useNavigate } from 'react-router-dom';

const InvoicesPage = () => {
  const [invoices, setInvoices] = useState([
    { id: 1, employee: 'John Doe', amount: 1200, date: '2024-05-01' },
    { id: 2, employee: 'Jane Smith', amount: 950, date: '2024-05-03' },
    { id: 3, employee: 'Alice Johnson', amount: 1500, date: '2024-05-05' },
    { id: 4, employee: 'Bob Brown', amount: 700, date: '2024-05-07' },
  ]);
  const [searchEmployee, setSearchEmployee] = useState('');

  const filteredInvoices = invoices.filter(invoice =>
    invoice.employee.toLowerCase().includes(searchEmployee.toLowerCase())
  );

  const navigate = useNavigate();
  const handleAddInvoice = () => {
    navigate('/sell');
  };

  return (
    <div className="invoices-page">
      <ToolBar />
      <h1 className="invoices-title">Invoices</h1>
      <div className="invoices-actions">
        <input
          type="text"
          placeholder="Search by employee"
          value={searchEmployee}
          onChange={e => setSearchEmployee(e.target.value)}
          className="invoices-search-input"
        />
        <button className="invoices-add-button" onClick={handleAddInvoice}>
          Add Invoice
        </button>
      </div>
      <ul className="invoices-list">
        {filteredInvoices.map(invoice => (
          <li key={invoice.id} className="invoice-item">
            <span className="invoice-employee">{invoice.employee}</span>
            <span className="invoice-amount">${invoice.amount}</span>
            <span className="invoice-date">{invoice.date}</span>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default InvoicesPage;