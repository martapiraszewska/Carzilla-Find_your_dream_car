import React, { useState, useEffect } from 'react';
import ToolBar from '../elements/ToolBar';
import './InvoicesPage.css';
import { useNavigate } from 'react-router-dom';

const InvoicesPage = () => {
  const [invoices, setInvoices] = useState([
    // { id: 1, employee: 'John Doe', amount: 1200, date: '2024-05-01' },
    // { id: 2, employee: 'Jane Smith', amount: 950, date: '2024-05-03' },
    // { id: 3, employee: 'Alice Johnson', amount: 1500, date: '2024-05-05' },
    // { id: 4, employee: 'Bob Brown', amount: 700, date: '2024-05-07' },
  ]);
  const [searchEmployee, setSearchEmployee] = useState('');

  const filteredInvoices = invoices.filter(invoice =>
    invoice.Name.toLowerCase().includes(searchEmployee.toLowerCase())
  );

  const navigate = useNavigate();
  const handleAddInvoice = () => {
    navigate('/sell');
  };

  const handleFetchInvoices = () => {
    const options = {
        method: 'GET',
        headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Headers': 'Origin, X-Requested-With, Content-Type, Accept', 'credentials': 'include'},
    };
    fetch('/invoices/search', options).then((response) => {
      if (response.status === 200) {
          response.json().then(data => {
            setInvoices(data);
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
    handleFetchInvoices();
  }, []);

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
          <li key={invoice.Invoice_ID} className="invoice-item">
            <span className="invoice-employee">{invoice.Name}</span>
            <span className="invoice-amount">{invoice.Value}$</span>
            <span className="invoice-date">{invoice.Date}</span>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default InvoicesPage;