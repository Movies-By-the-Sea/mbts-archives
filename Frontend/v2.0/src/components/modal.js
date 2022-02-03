import React from 'react'

const Modal = ({name, review, image, lead, director, year, id, overall, trailer, links, acting, story, execution, profundity, netflix, prime}) => {



    if({netflix}===1) {
        var stylesN = {
            net: {
                display: 'block'
            }
        } 
    } else {
        var stylesN = {
            net: {
                display: 'none'
            }
        }
    }

    if({prime}===1) {
        var stylesP = {
            pri: {
                display: 'block'
            }
        }
    } else {
        var stylesP = {
            pri: {
                display: 'none'
            }
        }
    }



    return (
        
        <>

        <div class="modal modal-full ie-scroll-fix" id={`modal-${id}`} tabindex="-1" role="dialog">
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                    <a href="#" class="close" role="button" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </a>
                    <div >
                        <div class="row">
                            <div class="col-md-8 offset-md-2">
                                
                            <br/><br/>


                                <nav aria-label="Breadcrumb navigation example">
                                    <ul class="breadcrumb">
                                        <li class="breadcrumb-item"><a href="#">Reviews</a></li>
                                        <li class="breadcrumb-item active" aria-current="page"><a href="#">{name}</a></li>
                                    </ul>
                                </nav>

                                <div className='modal_container'>

                                    <div>
                                        <div class="card p-0 w-300">
                                            <img src={image} class="img-fluid rounded-top" alt={name}></img>
                                            <div class="content">
                                                <div class="text-right d-flex"> 

                                                <div>
                                                    <a href={links} target='_blank'>
                                                    <img className='movie_link' src="https://img.icons8.com/bubbles/50/000000/domain.png"/>
                                                    </a>
                                                </div>
                                                <img className='movie_link' style={stylesN.net} src="https://img.icons8.com/bubbles/50/000000/netflix.png"/>
                                                <img className='movie_link' style={stylesP.pri} src="https://img.icons8.com/bubbles/50/000000/amazon.png"/>

                                                <div class="journal-info">
                                                    <a class="portfolio-link" data-toggle="modal" href={`#trailer${id}`}>Watch Trailer</a>
                                                </div> 

                                                </div>
                                            </div>
                                        </div>
                                    </div>

                                    

                                    <div>
                                        <h2 className='title'>{name}</h2> 
                                        <span className='text-muted'>Average Rating :    {overall}</span><br></br><br></br>
                                        <span className='text-muted'>Directed by :    {director}</span><br></br>
                                        <span className='text-muted'>Lead :    {lead}</span><br></br>
                                        <span className='text-muted'>Year of Release :    {year}</span><br></br><br></br>

                                        <p className='review'>{review}</p>
                                        <br/><br/>

                                        <br/><br/>

                                        <div className='d-flex'>
                                            <table class="table">
                                                <tbody>
                                                    <tr>
                                                        <th>Acting : </th>
                                                        <td>{acting}</td>
                                                    </tr>
                                                    <tr>
                                                        <th>Story : </th>
                                                        <td>{story}</td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                            <table class="table">
                                                <tbody>
                                                    <tr>
                                                        <th>Execution : </th>
                                                        <td>{execution}</td>
                                                    </tr>
                                                    <tr>
                                                        <td>
                                                            <th>Profundity : </th>
                                                            <td class="text-right">{profundity}</td>
                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </div>

                                        <br/><br/>


                                    </div>

                                </div>

                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="portfolio-modal modal fade" id={`trailer${id}`}  role="dialog" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content modal-trailer w-600">
                    <div class="container">
                        <div class="row">
                            <div class="modal-body w-600">
                                <iframe width="100%" height="315" src={trailer} frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        </>

    );
}

export default Modal