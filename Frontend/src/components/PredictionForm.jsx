import React, { useState } from 'react';

const PredictionForm = ({ onSubmit, isLoading }) => {
  const [formData, setFormData] = useState({
    age: 50,
    sex: "M",
    chest_pain_type: "TA",
    resting_bp: 120,
    cholesterol: 200,
    fasting_bs: 0,
    resting_ecg: "Normal",
    max_hr: 150,
    exercise_angina: "N",
    oldpeak: 0.0,
    st_slope: "Flat"
  });

  const handleChange = (e) => {
    const { name, value, type } = e.target;
    setFormData(prev => ({ 
      ...prev, 
      [name]: type === 'number' || name === 'fasting_bs' ? Number(value) : value 
    }));
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
            <label htmlFor="age">Age</label>
            <input type="number" id="age" name="age" value={formData.age} onChange={handleChange} required min="0" max="120" />
          </div>

          <div className="input-group">
            <label htmlFor="sex">Sex</label>
            <select id="sex" name="sex" value={formData.sex} onChange={handleChange}>
              <option value="M">Male</option>
              <option value="F">Female</option>
            </select>
          </div>

          <div className="input-group">
            <label htmlFor="chest_pain_type">Chest Pain Type</label>
            <select id="chest_pain_type" name="chest_pain_type" value={formData.chest_pain_type} onChange={handleChange}>
              <option value="TA">Typical Angina</option>
              <option value="ATA">Atypical Angina</option>
              <option value="NAP">Non-anginal Pain</option>
              <option value="ASY">Asymptomatic</option>
            </select>
          </div>

          <div className="input-group">
            <label htmlFor="resting_bp">Resting BP (mm/Hg)</label>
            <input type="number" id="resting_bp" name="resting_bp" value={formData.resting_bp} onChange={handleChange} required min="0" />
          </div>

          <div className="input-group">
            <label htmlFor="cholesterol">Serum Cholesterol (mg/dl)</label>
            <input type="number" id="cholesterol" name="cholesterol" value={formData.cholesterol} onChange={handleChange} required min="0" />
          </div>

          <div className="input-group">
            <label htmlFor="fasting_bs">Fasting Blood Sugar &gt; 120 mg/dl</label>
            <select id="fasting_bs" name="fasting_bs" value={formData.fasting_bs} onChange={handleChange}>
              <option value={0}>False</option>
              <option value={1}>True</option>
            </select>
          </div>

          <div className="input-group">
            <label htmlFor="resting_ecg">Resting ECG Results</label>
            <select id="resting_ecg" name="resting_ecg" value={formData.resting_ecg} onChange={handleChange}>
              <option value="Normal">Normal</option>
              <option value="ST">ST-T Wave Abnormality</option>
              <option value="LVH">LV Hypertrophy</option>
            </select>
          </div>

          <div className="input-group">
            <label htmlFor="max_hr">Max Heart Rate Achieved</label>
            <input type="number" id="max_hr" name="max_hr" value={formData.max_hr} onChange={handleChange} required min="60" max="220" />
          </div>

          <div className="input-group">
            <label htmlFor="exercise_angina">Exercise Induced Angina</label>
            <select id="exercise_angina" name="exercise_angina" value={formData.exercise_angina} onChange={handleChange}>
              <option value="N">No</option>
              <option value="Y">Yes</option>
            </select>
          </div>

          <div className="input-group">
            <label htmlFor="oldpeak">ST Depression (Oldpeak)</label>
            <input type="number" step="0.1" id="oldpeak" name="oldpeak" value={formData.oldpeak} onChange={handleChange} required />
          </div>

          <div className="input-group">
            <label htmlFor="st_slope">Peak Exercise ST Segment</label>
            <select id="st_slope" name="st_slope" value={formData.st_slope} onChange={handleChange}>
              <option value="Up">Upsloping</option>
              <option value="Flat">Flat</option>
              <option value="Down">Downsloping</option>
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
