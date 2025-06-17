import React, { useState } from 'react';
import './SearchBar.css';

const SearchBar = () => {
  const [brandInput, setBrandInput] = useState('');
  const [modelInput, setModelInput] = useState('');
  const [cars, setCars] = useState([]);
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState('');

  const handleSearch = () => {
    setLoading(true);
    setMessage('');
    const query = new URLSearchParams();
    if (brandInput) query.append('Brand', brandInput);
    if (modelInput) query.append('Model', modelInput);

    fetch(`/cars/search?${query.toString()}`)
      .then(response => {
        if (!response.ok) throw new Error('Failed to fetch cars');
        return response.json();
      })
      .then(data => {
        setCars(data);
        setLoading(false);
        if (!data.length) setMessage('No cars found');
      })
      .catch(error => {
        setMessage('Error fetching cars');
        setCars([]);
        setLoading(false);
      });
  };

  return (
    <div className="search-bar">
      <div className="input-group">
        <input
          type="text"
          placeholder="Enter brand"
          value={brandInput}
          onChange={(e) => setBrandInput(e.target.value)}
          className="brand-input"
        />
        <input
          type="text"
          placeholder="Enter model"
          value={modelInput}
          onChange={(e) => setModelInput(e.target.value)}
          className="model-input"
        />
        <button className="search-button" onClick={handleSearch}>
          Search
        </button>
      </div>
      <div className="car-list">
        {loading && <p>Loading...</p>}
        {message && <p>{message}</p>}
        {!loading && !message && cars.length > 0 && (
          <ul>
            {cars.map((car) => (
              <li key={car.Car_ID}>
                {car.Brand} {car.Model} - ${car.Price}
              </li>
            ))}
          </ul>
        )}
      </div>
    </div>
  );
};

export default SearchBar;