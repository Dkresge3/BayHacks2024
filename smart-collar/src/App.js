import React, {useState} from 'react';
import './App.css';
import Navbar from './components/Navbar';
import Home from './components/Home';
import Login from './components/Login';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Dog from './components/Dog';

function App() {
  const [navbarVisible, setNavbarVisible] = useState(true);

  const toggleNavbar = () => {
    setNavbarVisible(!navbarVisible);
  };

  return (
    <div className="App">
      
        <Navbar />
      
      <BrowserRouter>
				
				<div className='title'>
					
					
				</div>
				<Routes>
					<Route path="/" element={<Home />} />
					<Route path="/login" element={<Login />} />
          <Route path="/dog" element={<Dog />} />
				</Routes>
			</BrowserRouter>
    </div>
  );
}

export default App;
