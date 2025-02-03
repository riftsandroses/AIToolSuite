// import './App.css';
import { Box } from '@mui/material';
import TextField from '@mui/material/TextField';
import { BrowserRouter, Routes, Route } from 'react-router';
import Login from './Pages/Login/Login';
import Home from './Pages/Home/Home'

function App() {
  return (
    <div>
      <BrowserRouter>
        <Routes>
        <Route path="/test" element={<Home/>} />
          <Route path='/' element={<Login />} />
          <Route path="/home" element={<Home />} />
          {/* <Route path="/home" element={<Home />} /> */}
          {/* <Route path="/home" element={<Home />} /> */}
          {/* <Route path="/home" element={<Home />} /> */}


        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
