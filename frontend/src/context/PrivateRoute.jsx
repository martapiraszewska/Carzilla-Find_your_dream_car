import { Navigate } from 'react-router-dom';
import { useAuth } from './AuthContext';

const PrivateRoute = ({ children }) => {
  const { isLogged } = useAuth();

  return isLogged ? children : <Navigate to="/login" replace />;
};

export default PrivateRoute;