import React, { useState, useEffect } from 'react';
import Header from '../components/Header';
import PredictionForm from '../components/PredictionForm';
import ResultCard from '../components/ResultCard';
import AuthModal from '../components/AuthModal';
import '../App.css';
import { createPatient } from "../api/patients";
import { createPrediction } from "../api/predictions";

function Home() {
  const [result, setResult] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [isAuthOpen, setIsAuthOpen] = useState(false);
  const [userEmail, setUserEmail] = useState(null);

  useEffect(() => {
    const email = localStorage.getItem('user_email');
    if (email) setUserEmail(email);
  }, []);

  const handleLogout = () => {
    localStorage.removeItem('user_email');
    localStorage.removeItem('access_token');
    setUserEmail(null);
  };

  const handlePrediction = async (formData) => {
    const token = localStorage.getItem('access_token');
    if (!token) {
      alert("Please sign in to make a prediction.");
      setIsAuthOpen(true);
      return;
    }

    setIsLoading(true);
    
    try {
        const patientData = await createPatient(formData);
        const predictionData = await createPrediction(patientData.id);      

        setResult({
            prediction: predictionData.prediction,
            probability: predictionData.probability,
        });
    } catch (error) {
      console.error("Prediction error:", error);
      alert(error.message);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="ameba-layout">
      <Header 
        onSignInClick={() => setIsAuthOpen(true)} 
        userEmail={userEmail} 
        onLogout={handleLogout} 
      />
      <AuthModal 
        isOpen={isAuthOpen} 
        onClose={() => setIsAuthOpen(false)} 
        onLogin={(email) => setUserEmail(email)}
      />
      
      <section className="hero-section">
        <div className="particle-sphere"></div>
        <div className="hero-content">
          <div className="hero-eyebrow">Reactive to Proactive</div>
          <h1 className="hero-headline">Heart Disease Prediction</h1>
          <p className="hero-subtext">
            Analyze cardiovascular parameters and predict potential anomalies with our precise, data-driven intelligence layer.
          </p>
        </div>
      </section>

      <div className="section-transition"></div>

      <section id="predict" className="product-section">
        <div className="dashboard-mockup">
          <div className="dashboard-chrome">
            <div className="chrome-dot red"></div>
            <div className="chrome-dot yellow"></div>
            <div className="chrome-dot green"></div>
            <div className="chrome-url">app.heart-predictor.local</div>
          </div>
          
          <div className="dashboard-body">
            <aside className="dashboard-sidebar">
              <div className="sidebar-icon">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <rect x="3" y="3" width="7" height="7"></rect>
                  <rect x="14" y="3" width="7" height="7"></rect>
                  <rect x="14" y="14" width="7" height="7"></rect>
                  <rect x="3" y="14" width="7" height="7"></rect>
                </svg>
              </div>
              <div className="sidebar-icon">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <path d="M22 12h-4l-3 9L9 3l-3 9H2"></path>
                </svg>
              </div>
            </aside>
            
            <main className="dashboard-main">
              <PredictionForm onSubmit={handlePrediction} isLoading={isLoading} />
              <div id="results" className="dashboard-sidebar-right">
                <ResultCard result={result} />
              </div>
            </main>
          </div>
        </div>
      </section>
    </div>
  );
}

export default Home;
