import React, {useState} from 'react';
import './CarsPage.css';
import SearchBar from '../elements/SearchBar';
import ToolBar from '../elements/ToolBar';

const Cars = () => {
  const [stats, setStats] = useState([]);

  const handleAddCar = () => {
    alert('Add Car functionality coming soon!');
  //   const options = {
  //       method: 'GET',
  //       headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Headers': 'Origin, X-Requested-With, Content-Type, Accept', 'credentials': 'include'},
  //   };
  //   fetch('/profile/search', options).then((response) => {
  //     if (response.status === 200) {
  //         console.log(response);
  //         response.json().then(data => {
  //           setStats(data);
  //           console.log(data);
  //         })
  //     }
  //     else{
  //         console.log("unable to fetch profile data", response);
  //     }
  //   });
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