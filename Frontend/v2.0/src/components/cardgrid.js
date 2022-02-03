import React from 'react';
import Cards from './cards';

const CardList = ({reviews}) => {
    const cardArray = reviews.map((user, i) => {
        return  (
        
        <Cards 
        Name={reviews[i].Name} 
        Overall={reviews[i].Overall} 
        Image={reviews[i].Image} 
        Genre1={reviews[i].Genre1}
        Genre2={reviews[i].Genre2} 
        Review={reviews[i].Review}
        Lead={reviews[i].Lead}
        Director={reviews[i].Director}
        Year={reviews[i].Year}
        ID={reviews[i].ID} 
        Trailer={reviews[i].Trailer}
        Links={reviews[i].Links}
        Acting={reviews[i].Acting}
        Story={reviews[i].Story}
        Execution={reviews[i].Execution}
        Profundity={reviews[i].Profundity}
        Netflix={reviews[i].Netflix}
        Prime={reviews[i].Prime}
        />

        );
    })
    return (
        <div className='d-flex flex-wrap'>
        {cardArray}
        <p className='ending_line'>Will keep on adding new movies!</p><br></br><br></br>
      </div>
    );
}

export default CardList