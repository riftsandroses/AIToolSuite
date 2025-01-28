// import './App.css';
import { Box } from '@mui/material';
import TextField from '@mui/material/TextField';
import { BrowserRouter, Routes, Route } from 'react-router';
import Login from './Pages/Login/Login';
import Dashboard from './Pages/Dashboard/Dashboard'

function App() {
  return (
    <div>
      <BrowserRouter>
        <Routes>
        <Route path="/test" element={<Dashboard/>} />
          <Route path="/" element={<Login />} />
          <Route path='/login' element={<Login />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
