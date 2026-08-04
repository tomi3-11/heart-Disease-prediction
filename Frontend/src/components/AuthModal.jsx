import React, { useState } from 'react';
import { login, register } from "../api/auth"

const AuthModal = ({ isOpen, onClose, onLogin }) => {
  const [isSignUp, setIsSignUp] = useState(false);
  const [error, setError] = useState('');

  if (!isOpen) return null;

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    const email = e.target.email.value;
    const password = e.target.password.value;
    
    const url = isSignUp 
      ? `${import.meta.env.VITE_API_URL}/auth/register` 
      : `${import.meta.env.VITE_API_URL}/auth/login`;

    const body = isSignUp 
      ? { email, password, role: 'doctor' }
      : { email, password };

    try {
        let data;

        if (isSignUp) {
            await register(email, password);
            setIsSignUp(false);
            setError("Account created. Please log in.");
            return;
        }

        data = await login(email, password);

        localStorage.setItem("access_token", data.access_token);
        localStorage.setItem("user_email", email);

        if (onLogin) {
            onLogin(email);
        }

        onClose();
    } catch (err) {
        setError(
            err.response?.data?.detail ||
            err.message ||
            "Authentication failed"
        );
    }
  };

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
        
        {error && <div style={{ color: 'var(--danger-red)', marginBottom: '1rem', fontSize: '14px' }}>{error}</div>}

        <form className="auth-form" onSubmit={handleSubmit}>
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
          <span className="auth-toggle-link" onClick={() => { setIsSignUp(!isSignUp); setError(''); }}>
            {isSignUp ? 'Sign In' : 'Sign Up'}
          </span>
        </div>
      </div>
    </div>
  );
};

export default AuthModal;
