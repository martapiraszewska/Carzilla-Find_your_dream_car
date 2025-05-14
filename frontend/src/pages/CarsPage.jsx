import React, { useState } from 'react';
import './CarsPage.css';
import ToolBar from '../elements/ToolBar';
import { useNavigate } from 'react-router-dom';

const CarsPage = () => {
  const [cars, setCars] = useState([
    { id: 1, brand: 'Toyota', model: 'Corolla', year: 2020, price: 15000 },
    { id: 2, brand: 'Honda', model: 'Civic', year: 2019, price: 14000 },
    { id: 3, brand: 'Ford', model: 'Focus', year: 2018, price: 12000 },
    { id: 4, brand: 'BMW', model: '3 Series', year: 2021, price: 25000 },
  ]);
  const [showSearch, setShowSearch] = useState(false);
  const [searchBrand, setSearchBrand] = useState('');
  const [searchModel, setSearchModel] = useState('');
  const navigate = useNavigate();

  const handleSellCar = (carId) => {
    navigate(`/sell-car/${carId}`);
  };

  const handleRemoveCar = (carId) => {
    setCars((prev) => prev.filter((car) => car.id !== carId));
  };

  // Filter cars based on search input
  const filteredCars = cars.filter(car =>
    car.brand.toLowerCase().includes(searchBrand.toLowerCase()) &&
    car.model.toLowerCase().includes(searchModel.toLowerCase())
  );

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
      <ul className="cars-list">
        {filteredCars.map((car) => (
          <li key={car.id} className="car-item">
            <span className="car-info">
              {car.brand} {car.model} ({car.year}) - {car.price}$
            </span>
            <div className="car-actions">
              <button className="cars-button" onClick={() => handleSellCar(car.id)}>
                Sell
              </button>
              <button className="cars-button remove" onClick={() => handleRemoveCar(car.id)}>
                Remove
              </button>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default CarsPage;