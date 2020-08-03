import React from 'react';

import logoImg from '../../assets/images/logo.svg';
import landingImg from '../../assets/images/landing.svg';
import studyIcon from '../../assets/images/icons/study.svg';
import giveClassesIcon from '../../assets/images/icons/give-classes.svg';
import purplerHeartIcon from '../../assets/images/icons/purple-heart.svg';

import './styles.css';

const Landing = () => {
  return (
    <div id="page-landing">
      <div id="page-landing-content" className="container">
        <div className="logo-container">
          <img src={logoImg} alt="Proffy" />
          <h2>Sua plataforma de estudos online.</h2>
        </div>
        <img src={landingImg} alt="plataforma de estudos" className="hero-image" />
        <div className="buttons-container">
          <a href="" className="study">
            <img src={studyIcon} alt="Estudar" />
          </a>

          <a href="" className="give-classes">
            <img src={giveClassesIcon} alt="Ensinar" />
          </a>
        </div>
        <span className="total-connections">
          Total de 200 conexões já realizadas
          {' '}
          <img src={purplerHeartIcon} alt="Coração roxo" />
        </span>
      </div>
    </div>
  );
};

export default Landing;
