import React, { useState, useEffect } from 'react';
import './CarsPage.css';
import ToolBar from '../elements/ToolBar';
import { useNavigate } from 'react-router-dom';

const CarsPage = () => {
  const [cars, setCars] = useState([]);
  const [showSearch, setShowSearch] = useState(false);
  const [searchBrand, setSearchBrand] = useState('');
  const [searchModel, setSearchModel] = useState('');
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState('');
  const navigate = useNavigate();

  // Fetch all cars on mount
  useEffect(() => {
    fetchCars();
  }, []);

  // Fetch cars from backend (all or with search)
  const fetchCars = (brand = '', model = '') => {
    setLoading(true);
    setMessage('');
    let url = '/cars/search';
    const params = [];
    if (brand) params.push(`Brand=${encodeURIComponent(brand)}`);
    if (model) params.push(`Model=${encodeURIComponent(model)}`);
    if (params.length) url += '?' + params.join('&');
    fetch(url)
      .then((res) => {
        if (!res.ok) throw new Error('Failed to fetch cars');
        return res.json();
      })
      .then((data) => {
        setCars(data);
        setLoading(false);
      })
      .catch(() => {
        setMessage('Error loading cars.');
        setCars([]);
        setLoading(false);
      });
  };

  // Handle search
  useEffect(() => {
    if (showSearch) {
      fetchCars(searchBrand, searchModel);
    }
    // eslint-disable-next-line
  }, [searchBrand, searchModel]);

  const handleSellCar = (carId) => {
    navigate(`/sell`);
  };

  const handleRemoveCar = (carId) => {
    setMessage('');
    fetch(`/cars/remove/${carId}`, {
      method: 'DELETE',
      headers: { 'Content-Type': 'application/json' },
    })
      .then(async (res) => {
        if (!res.ok) {
          const data = await res.json();
          throw new Error(data.error || 'Failed to remove car');
        }
        setCars((prev) => prev.filter((car) => car.Car_ID !== carId));
        setMessage('Car removed successfully.');
      })
      .catch(() => {
        setMessage('Error removing car.');
      });
  };

  return (
    <div className="cars-page">
      <ToolBar />
      <div className="cars-actions-top">
        <button
          className="cars-button"
          onClick={() => setShowSearch((prev) => !prev)}
        >
          Search Car
        </button>
        <button className="cars-button" onClick={() => navigate('/add-car')}>
          Add Car
        </button>
      </div>
      {showSearch && (
        <div className="cars-search-box">
          <input
            type="text"
            placeholder="Brand"
            value={searchBrand}
            onChange={(e) => setSearchBrand(e.target.value)}
            className="cars-search-input"
          />
          <input
            type="text"
            placeholder="Model"
            value={searchModel}
            onChange={(e) => setSearchModel(e.target.value)}
            className="cars-search-input"
          />
        </div>
      )}
      {loading && <div>Loading cars...</div>}
      {message && <div className="cars-message">{message}</div>}
      <ul className="cars-list">
        {cars.map((car) => (
          <li key={car.Car_ID} className="car-item">
            <span className="car-info">
              {car.Brand} {car.Model} ({car.Color}) - {car.Price}$
            </span>
            <div className="car-actions">
              <button className="cars-button" onClick={() => handleSellCar(car.Car_ID)}>
                Sell
              </button>
              <button className="cars-button remove" onClick={() => handleRemoveCar(car.Car_ID)}>
                Remove
              </button>
            </div>
          </li>
        ))}
      </ul>
      {!loading && cars.length === 0 && <div>No cars found.</div>}
    </div>
  );
};

export default CarsPage;