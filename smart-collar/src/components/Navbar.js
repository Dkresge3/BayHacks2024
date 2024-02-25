import React from 'react';
import './Navbar.css'


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
          <a href='Dog'> Dog</a>
        </li>
      </ul>
      
    </nav>
  );
}

export default Navbar;