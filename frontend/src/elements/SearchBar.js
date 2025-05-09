import React, { useState } from 'react';
import './SearchBar.css';

const SearchBar = () => {
  const [query, setQuery] = useState('');
  const [queryData, setData] = useState([]);  // not ideal way to do this

  function querySearch(){
    fetch(`search?${query}`)
      .then(response => {
        console.log(response);
        return response.json();
      })
      .then(data => {
        setData(data);
      })
      .catch(error => console.error('Error:', error));
  }

  return (
    <div className="search-bar">
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Search... can be empty"
        className="search-input"
      />
      <button className="search-button" onClick={querySearch}> Search</button>
      {queryData.map(d => ` |${d.brand}|`)}  {/*another not good thing*/}
    </div>
  );
};

export default SearchBar;