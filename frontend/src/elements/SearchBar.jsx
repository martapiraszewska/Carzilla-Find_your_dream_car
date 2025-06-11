import React, { useState } from 'react';
import './SearchBar.css';

const SearchBar = () => {
  const [brandInput, setBrandInput] = useState('');
  const [modelInput, setModelInput] = useState('');
  const [cars, setCars] = useState([]);

  const handleSearch = () => {
    const query = new URLSearchParams();
    if (brandInput) query.append('brand', brandInput);
    if (modelInput) query.append('model', modelInput);

    fetch(`cars/search?${query.toString()}`)
      .then(response => response.json())
      .then(data => {
        setCars(data);
      })
      .catch(error => console.error('Error fetching cars:', error));
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
        {cars.length > 0 ? (
          <ul>
            {cars.map((car) => (
              <li key={car.id}>
                {car.Brand} {car.Model} - ${car.Price}
              </li>
            ))}
          </ul>
        ) : (
          <p>No cars found</p>
        )}
      </div>
    </div>
  );
};

export default SearchBar;