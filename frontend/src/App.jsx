import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';
import HomePage from './pages/HomePage';
import LoginPage from './pages/LoginPage';
import DashboardPage from './pages/DashboardPage';
import ProfilePage from './pages/ProfilePage';
import CarsPage from './pages/CarsPage';
import EmployeePage from './pages/EmployeePage';
import InvoicesPage from './pages/InvoicesPage';
// import ClientsPage from './pages/ClientsPage';
// import StatsPage from './pages/StatsPage';
import AddEmployee from './forms/AddEmployee';
import AddCar from './forms/AddCar';
import AddInvoice from './forms/AddInvoice';

const App = () => {
  return (
    <AuthProvider>
      <Router>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/dashboard" element={<DashboardPage />} />
          <Route path="/profile" element={<ProfilePage />} />
          <Route path="/cars" element={<CarsPage />} />
          <Route path="/employees" element={<EmployeePage />} />
          <Route path="/invoices" element={<InvoicesPage />} />
          <Route path="/hire" element={<AddEmployee />} />
          <Route path="/add-car" element={<AddCar />} />
          <Route path="/sell" element={<AddInvoice />} />
        </Routes>
      </Router>
    </AuthProvider>
  );
};

export default App;