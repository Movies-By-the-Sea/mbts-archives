import React from 'react';

const Navbar = () => {

    return (
      <>
        <nav class="navbar sticky">
        <a href="#" class="navbar-brand">
          <h3 className='nav_heading'>Movies By the Sea</h3>
          <img src='https://github.com/Saumya-Bhatt/movies.by.the.sea/blob/master/static/images/web%20bar.png?raw=true' className='nav_image'></img>
        </a>
        <ul class="navbar-nav ml-auto">
          <li class="nav-item">
            <a href="#" class="nav-link">About</a>
          </li>
          <li class="nav-item">
            <a href="#" class="nav-link">Reviews</a>
          </li>
          <li class="nav-item">
            <a href="#" class="nav-link">Contact</a>
          </li>
        </ul>
      </nav>

    </>
    );
}

export default Navbar