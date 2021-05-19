import React from 'react';
import Modal from './modal';

const Cards = ({Name, Overall, Genre1, Genre2, Image, Lead, Review, Director, Year, ID, Trailer, Links, Acting, Story, Execution, Profundity, Netflix, Prime}) => { 

    return (

        <>

        <div class="w-350 mw-full d-flex-fill">
            <div class="card external_card p-0">
                <a href={`#modal-${ID}`} className=' card_image' role="button">
                    <img src={Image} class="img-fluid rounded-top .w-400 .h-250" alt={Name}/>
                </a>
                <div class="content">
                    <p class="text-muted">
                        <b>Genre : </b>{Genre1} , {Genre2} <br/>
                        <b>Average Rating : </b>{Overall}
                    </p>

                </div>
            </div>
        </div>

        <Modal 
        name={Name} 
        image={Image}
        director={Director}
        review={Review}
        lead={Lead}
        year={Year}
        id={ID}
        overall={Overall}
        trailer={Trailer}
        links={Links}
        acting={Acting}
        story={Story}
        execution={Execution}
        profundity={Profundity}
        netflix={Netflix}
        prime={Prime}
        />


        </>
    );
}

export default Cards