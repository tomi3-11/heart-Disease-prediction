import React from 'react';

const Header = ({ onSignInClick }) => {
  return (
    <header className="ameba-nav">
      <div className="ameba-nav-left">
        <div className="logo">Heart Predictor</div>
      </div>
      <div className="ameba-nav-center">
        <a>Product</a>
        <a>Customer Types</a>
        <a>Company</a>
        <a>Resources</a>
        <a>Security</a>
      </div>
      <div className="ameba-nav-right">
        <button className="primary-cta" onClick={onSignInClick}>Sign In</button>
      </div>
    </header>
  );
};

export default Header;
