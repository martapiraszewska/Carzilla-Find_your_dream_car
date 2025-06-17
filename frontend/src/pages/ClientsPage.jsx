import React, { useState, useEffect } from 'react';
import ToolBar from '../elements/ToolBar';
import './ClientsPage.css';
import { useNavigate } from 'react-router-dom';

const ClientsPage = () => {
  const [clients, setClients] = useState([]);
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    setLoading(true);
    setMessage('');
    fetch('/clients/search')
      .then((res) => {
        if (!res.ok) throw new Error('Failed to fetch clients');
        return res.json();
      })
      .then((data) => {
        setClients(data);
        setLoading(false);
      })
      .catch(() => {
        setMessage('Error loading clients.');
        setClients([]);
        setLoading(false);
      });
  }, []);

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
      {loading && <div>Loading clients...</div>}
      {message && <div className="clients-message">{message}</div>}
      <ul className="clients-list">
        {clients.map(client => (
          <li key={client.Client_ID} className="client-item">
            <span className="client-name">{client.Name} {client.Surname}</span>
            <span className="client-email">{client.Mail}</span>
            <span className="client-phone">{client.Phone}</span>
          </li>
        ))}
      </ul>
      {!loading && clients.length === 0 && <div>No clients found.</div>}
    </div>
  );
};

export default ClientsPage;