import React from 'react';

const Header = () => {
    return (
        <>
        <div class="container dead_poet">
            <div class="float-left d-inline-block">
                <div className='header'>
                    <p>"Medicine, law, business, engineering, these are noble pursuits <br></br>
                    and necessary to sustain life. But</p>
                    <h1>poetry, beauty, romance, love,</h1>
                    <p>these are what we stay alive for."</p>
                    <div className='mobile_quote'>- Dead Poet's Society</div>
                </div>
            </div>
            <div className='williams'>
                <img className='robbie' src='https://image.flaticon.com/icons/png/512/110/110436.png'></img>
                <p> - Robbin Williams <br></br>Dead Poet's Society</p>
            </div>
        </div>
        <br></br>
        <div className='container inst'>
            <p>Click on the posters below to read the complete review and get access to links to watch those films online free.</p>
        </div>
        <div className='container'>
            <div className='line'></div>
        </div>
        </>
    );
}

export default Header