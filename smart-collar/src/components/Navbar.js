import React from 'react';
import './Navbar.css'
import Home from './Home';
import Login from './Login';

function Navbar() {
  return (
    <nav className="nav">
      <h1 className='site-title'>
        Smart Collar
        </h1>
      <ul>
        <li>
          <a href='Home'>Home</a>
          <a href='Login'> Login</a>
        </li>
      </ul>
      
    </nav>
  );
}

export default Navbar;