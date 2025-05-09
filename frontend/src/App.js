import React  from 'react';
import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import HomePage from './pages/HomePage.js';
import LoginPage from './pages/LoginPage.js';


function App() {
  return (
    <div className='App'>
      <Router>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/login" element={<LoginPage />} />
        </Routes>
      </Router>
    </div>
  );
}

// function App() {
//   return (
//     <div className="App">
//       <div>
//         <ToolBar></ToolBar>
//       </div>
//       <div>
//         <SearchBar></SearchBar>
//       </div>
//     </div>
//   );
// }

export default App;
