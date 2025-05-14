import React, { useState } from 'react';
import ToolBar from '../elements/ToolBar';
import './ClientsPage.css';
import { useNavigate } from 'react-router-dom';
const ClientsPage = () => {
  const [clients, setClients] = useState([
    { id: 1, name: 'Jane Smith', email: 'jane.smith@email.com', phone: '123-456-789' },
    { id: 2, name: 'John Doe', email: 'john.doe@email.com', phone: '987-654-321' },
    { id: 3, name: 'Alice Johnson', email: 'alice.j@email.com', phone: '555-123-456' },
    { id: 4, name: 'Bob Brown', email: 'bob.brown@email.com', phone: '444-555-666' },
  ]);

  const navigate = useNavigate();
  const handleAddClient = () => {
    navigate('/add-client');
  };

  return (
    <div className="clients-page">
      <ToolBar />
      <h1 className="clients-title">Clients</h1>
      <button className="clients-add-button" onClick={handleAddClient}>
        Add Client
      </button>
      <ul className="clients-list">
        {clients.map(client => (
          <li key={client.id} className="client-item">
            <span className="client-name">{client.name}</span>
            <span className="client-email">{client.email}</span>
            <span className="client-phone">{client.phone}</span>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ClientsPage;