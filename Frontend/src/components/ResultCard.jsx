import React from 'react';

const ResultCard = ({ result }) => {
  if (!result) {
    return (
      <div className="stat-card">
        <div className="stat-label">Prediction Status</div>
        <div className="stat-value">Pending...</div>
        <div className="status-tag pending">AWAITING DATA</div>
      </div>
    );
  }

  const isHighRisk = result.prediction === 1;

  return (
    <div className="stat-card">
      <div className="stat-label">Risk Assessment Probability</div>
      <div className="stat-value">{(result.probability * 100).toFixed(1)}%</div>
      <div className={`status-tag ${isHighRisk ? 'critical' : 'nominal'}`}>
        {isHighRisk ? 'Heart Disease Detected' : 'No Heart Disease Detected'}
      </div>
      <p style={{ marginTop: '1rem', fontSize: '14px', color: 'var(--color-slate-body)', lineHeight: '1.5' }}>
        {isHighRisk 
          ? "Anomalous indicators detected in cardiovascular data. Medical consultation recommended."
          : "All cardiovascular parameters within nominal range. Continue current lifecycle habits."}
      </p>
    </div>
  );
};

export default ResultCard;
