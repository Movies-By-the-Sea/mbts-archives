import React, {Component} from 'react';
import './Extra/App.css';
import Navbar from './components/navbar';
import CardList from './components/cardgrid';
import reviews from './Extra/reviews.json';
import Header from './components/Header';
import Footer from './components/Footer'

class App extends Component {
  render() {
    return (
      <>
      <div className='page-wrapper'>
        <div className='content-wrapper'>

          <Navbar />
          <Header />
          <div class='container'>
            <CardList reviews = {reviews}  />
          </div>
          <Footer />
        </div>
      </div>
      </>
    ); 
  }
}


export default App;
