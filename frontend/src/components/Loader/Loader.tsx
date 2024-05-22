import React from 'react';
import './Loader.css';

const StarLoader: React.FC = () => {
    return (
      <div className="loader-container">
        <div className="loader">
          <div className="star star1"></div>
          <div className="star star2"></div>
          <div className="star star3"></div>
          <div className="star star4"></div>
          <div className="star star5"></div>
          <div className="star star6"></div>
          <div className="star star7"></div>
          <div className="star star8"></div>
        </div>
      </div>
    );
  };
  
  export default StarLoader;
