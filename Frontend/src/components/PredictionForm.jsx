import React, { useState } from 'react';

const PredictionForm = ({ onSubmit, isLoading }) => {
  const [formData, setFormData] = useState({
    Age: 50,
    Sex: 1,
    ChestPainType: 0,
    RestingBP: 120,
    Cholesterol: 200,
    FastingBS: 0,
    RestingECG: 0,
    MaxHR: 150,
    ExerciseAngina: 0,
    Oldpeak: 0.0,
    ST_Slope: 1
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: Number(value) }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(formData);
  };

  return (
    <div className="form-container">
      <div className="panel-title">Patient Parameters</div>
      <form onSubmit={handleSubmit}>
        <div className="form-grid">
          
          <div className="input-group">
            <label htmlFor="Age">Age</label>
            <input type="number" id="Age" name="Age" value={formData.Age} onChange={handleChange} required min="0" max="120" />
          </div>

          <div className="input-group">
            <label htmlFor="Sex">Sex</label>
            <select id="Sex" name="Sex" value={formData.Sex} onChange={handleChange}>
              <option value={1}>Male</option>
              <option value={0}>Female</option>
            </select>
          </div>

          <div className="input-group">
            <label htmlFor="ChestPainType">Chest Pain Type</label>
            <select id="ChestPainType" name="ChestPainType" value={formData.ChestPainType} onChange={handleChange}>
              <option value={0}>Typical Angina</option>
              <option value={1}>Atypical Angina</option>
              <option value={2}>Non-anginal Pain</option>
              <option value={3}>Asymptomatic</option>
            </select>
          </div>

          <div className="input-group">
            <label htmlFor="RestingBP">Resting BP (mm/Hg)</label>
            <input type="number" id="RestingBP" name="RestingBP" value={formData.RestingBP} onChange={handleChange} required min="0" />
          </div>

          <div className="input-group">
            <label htmlFor="Cholesterol">Serum Cholesterol (mg/dl)</label>
            <input type="number" id="Cholesterol" name="Cholesterol" value={formData.Cholesterol} onChange={handleChange} required min="0" />
          </div>

          <div className="input-group">
            <label htmlFor="FastingBS">Fasting Blood Sugar &gt; 120 mg/dl</label>
            <select id="FastingBS" name="FastingBS" value={formData.FastingBS} onChange={handleChange}>
              <option value={0}>False</option>
              <option value={1}>True</option>
            </select>
          </div>

          <div className="input-group">
            <label htmlFor="RestingECG">Resting ECG Results</label>
            <select id="RestingECG" name="RestingECG" value={formData.RestingECG} onChange={handleChange}>
              <option value={0}>Normal</option>
              <option value={1}>ST-T Wave Abnormality</option>
              <option value={2}>LV Hypertrophy</option>
            </select>
          </div>

          <div className="input-group">
            <label htmlFor="MaxHR">Max Heart Rate Achieved</label>
            <input type="number" id="MaxHR" name="MaxHR" value={formData.MaxHR} onChange={handleChange} required min="60" max="220" />
          </div>

          <div className="input-group">
            <label htmlFor="ExerciseAngina">Exercise Induced Angina</label>
            <select id="ExerciseAngina" name="ExerciseAngina" value={formData.ExerciseAngina} onChange={handleChange}>
              <option value={0}>No</option>
              <option value={1}>Yes</option>
            </select>
          </div>

          <div className="input-group">
            <label htmlFor="Oldpeak">ST Depression (Oldpeak)</label>
            <input type="number" step="0.1" id="Oldpeak" name="Oldpeak" value={formData.Oldpeak} onChange={handleChange} required />
          </div>

          <div className="input-group">
            <label htmlFor="ST_Slope">Peak Exercise ST Segment</label>
            <select id="ST_Slope" name="ST_Slope" value={formData.ST_Slope} onChange={handleChange}>
              <option value={0}>Upsloping</option>
              <option value={1}>Flat</option>
              <option value={2}>Downsloping</option>
            </select>
          </div>

          <button type="submit" className="primary-cta" disabled={isLoading}>
            {isLoading ? 'Analyzing Parameters...' : 'Execute Prediction'}
          </button>
        </div>
      </form>
    </div>
  );
};

export default PredictionForm;
