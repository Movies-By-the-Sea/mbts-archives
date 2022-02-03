import React from 'react'

const Footer = () => {
    return(
        <nav class="navbar navbar-fixed-bottom">
            <div className='container'>
            <div class="navbar-content">
                <div class="navbar-brand footer ml-auto">
                    <i className='fa fa-instagram'>
                        <a href='https://www.instagram.com/movies.by.the.sea/'></a>
                    </i>
                    <i class="fa fa-facebook">
                        <a href='https://www.facebook.com/MoviesbytheSea/?modal=admin_todo_tour'></a>
                    </i>
                    <i className='fa fa-envelope'>
                        <a href='mailto:saumya.bhatt106@gmail.com'></a>
                    </i>
                </div>
            </div>
            <div class="navbar-brand footer ml-auto">
                <p>Designed by Saumya Bhatt</p>
            </div>
            </div>
      </nav>
    );
}

export default Footer