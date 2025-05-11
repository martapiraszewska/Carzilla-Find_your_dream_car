import React from 'react';
import './CarsPage.css';
import SearchBar from '../elements/SearchBar';
import ToolBar from '../elements/ToolBar';

const Cars = () => {
  const handleAddCar = () => {
    alert('Add Car functionality coming soon!');
  };

  const handleRemoveCar = () => {
    alert('Remove Car functionality coming soon!');
  };

  return (
    <div className="cars-page">
      <ToolBar />
      <h1 className="cars-title">Manage Cars</h1>
      <SearchBar />
      <div className="cars-actions">
        <button className="cars-button" onClick={handleAddCar}>
          Add Car
        </button>
        <button className="cars-button" onClick={handleRemoveCar}>
          Remove Car
        </button>
      </div>
    </div>
  );
};

export default Cars;