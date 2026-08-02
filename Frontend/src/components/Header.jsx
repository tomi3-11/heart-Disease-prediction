import React from 'react';

const Header = ({ onSignInClick, userEmail, onLogout }) => {
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
        {userEmail ? (
          <div style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
            <span style={{ fontSize: '14px', color: 'var(--color-fog)' }}>{userEmail}</span>
            <button className="primary-cta" onClick={onLogout} style={{ background: 'transparent', border: '1px solid var(--color-fog)', color: 'var(--color-paper)' }}>Log Out</button>
          </div>
        ) : (
          <button className="primary-cta" onClick={onSignInClick}>Sign In</button>
        )}
      </div>
    </header>
  );
};

export default Header;
