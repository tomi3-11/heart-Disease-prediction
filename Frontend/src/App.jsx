import React, { useState } from 'react';
import Header from './components/Header';
import PredictionForm from './components/PredictionForm';
import ResultCard from './components/ResultCard';
import AuthModal from './components/AuthModal';
import './App.css';

function App() {
  const [result, setResult] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [isAuthOpen, setIsAuthOpen] = useState(false);

  const handlePrediction = async (formData) => {
    setIsLoading(true);
    
    try {
      // TODO: BACKEND INTEGRATION
      // 1. Replace the setTimeout below with an actual fetch/axios call to your Node.js API
      // e.g., const response = await fetch('http://localhost:3000/api/predict', { method: 'POST', body: JSON.stringify(formData) })
      // 2. Parse the response
      // e.g., const data = await response.json()
      // 3. Call setResult with the backend's prediction (1 = high risk, 0 = low risk) and probability
      // e.g., setResult({ prediction: data.prediction, probability: data.probability })
      
      // --- SIMULATED API CALL (REMOVE THIS) ---
      await new Promise(resolve => setTimeout(resolve, 1500));
      
      const score = (formData.Age / 100) + (formData.Cholesterol / 500) + (formData.MaxHR < 120 ? 0.3 : 0);
      const isHighRisk = score > 1.2;
      
      setResult({
        prediction: isHighRisk ? 1 : 0,
        probability: isHighRisk ? 0.85 : 0.15
      });
      // ----------------------------------------
      
    } catch (error) {
      console.error("Prediction error:", error);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="ameba-layout">
      <Header onSignInClick={() => setIsAuthOpen(true)} />
      <AuthModal isOpen={isAuthOpen} onClose={() => setIsAuthOpen(false)} />
      
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

      <section className="product-section">
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
              <div className="dashboard-sidebar-right">
                <ResultCard result={result} />
              </div>
            </main>
          </div>
        </div>
      </section>
    </div>
  );
}

export default App;
