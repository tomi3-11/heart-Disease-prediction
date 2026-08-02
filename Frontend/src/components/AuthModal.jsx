import React, { useState } from 'react';

const AuthModal = ({ isOpen, onClose }) => {
  const [isSignUp, setIsSignUp] = useState(false);

  if (!isOpen) return null;

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content frosted-panel" onClick={(e) => e.stopPropagation()}>
        <div className="modal-header">
          <div className="hero-eyebrow">{isSignUp ? 'Create Account' : 'Authenticate'}</div>
          <button className="close-btn" onClick={onClose}>
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <line x1="18" y1="6" x2="6" y2="18"></line>
              <line x1="6" y1="6" x2="18" y2="18"></line>
            </svg>
          </button>
        </div>
        
        <form className="auth-form" onSubmit={(e) => {
          e.preventDefault();
          // TODO: BACKEND INTEGRATION
          // Handle Authentication here (fetch to Node.js backend)
          // const email = e.target.email.value;
          // const password = e.target.password.value;
          // if (isSignUp) { 
          //    await fetch('/api/signup', ...) 
          // } else { 
          //    await fetch('/api/login', ...) 
          // }
          onClose();
        }}>
          <div className="input-group">
            <label htmlFor="email">Email Address</label>
            <input type="email" id="email" name="email" required />
          </div>
          
          <div className="input-group">
            <label htmlFor="password">Password</label>
            <input type="password" id="password" name="password" required />
          </div>

          <button type="submit" className="primary-cta" style={{ width: '100%', marginTop: 'var(--spacing-20)' }}>
            {isSignUp ? 'Create Account' : 'Sign In'}
          </button>
        </form>

        <div className="auth-toggle">
          {isSignUp ? 'Already have an account? ' : 'Need an account? '}
          <span className="auth-toggle-link" onClick={() => setIsSignUp(!isSignUp)}>
            {isSignUp ? 'Sign In' : 'Sign Up'}
          </span>
        </div>
      </div>
    </div>
  );
};

export default AuthModal;
